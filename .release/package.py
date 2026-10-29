"""Package an already validated compiled update without accessing private source or credentials."""
from pathlib import Path
import hashlib, json, shutil, subprocess, tarfile, zipfile, os, time

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / 'release-output'
WORK = ROOT / 'release-work'
VERSION = '0.1.0-8'
BASE_SHA = '13a7928f6c557fff0819c8a057264a409531cb72f1376a593ccfc78ec23cfcd4'
BASE_URL = 'https://github.com/xHitech/music-manga-linux/releases/download/v0.1.0/music-manga-0.1.0-linux-x64.tar.gz'
for directory in [OUT, WORK]:
    if directory.exists(): shutil.rmtree(directory)
    directory.mkdir()
base = WORK / 'base.tar.gz'
subprocess.run(['curl', '--fail', '--location', '--retry', '3', '--output', str(base), BASE_URL], check=True)
assert hashlib.sha256(base.read_bytes()).hexdigest() == BASE_SHA, 'Base release checksum mismatch'
with tarfile.open(base) as source:
    for member in source.getmembers():
        assert member.name == 'music-manga' or member.name.startswith('music-manga/')
        assert '..' not in Path(member.name).parts
    source.extractall(WORK, filter='tar')
app = WORK / 'music-manga'
main_jar = next((app / 'lib/app').glob('composeApp-desktop-*.jar'))
old_jar = WORK / 'old.jar'
main_jar.rename(old_jar)
with zipfile.ZipFile(old_jar) as old, zipfile.ZipFile(ROOT / '.release/payload.zip') as patch, zipfile.ZipFile(main_jar, 'w', zipfile.ZIP_DEFLATED) as new:
    deleted = set(json.loads(patch.read('release-deleted.json')))
    updates = set(patch.namelist()) - {'release-deleted.json'}
    for entry in old.infolist():
        if entry.filename not in deleted and entry.filename not in updates:
            new.writestr(entry, old.read(entry.filename))
    for name in sorted(updates):
        new.writestr(patch.getinfo(name), patch.read(name))
manifest = json.loads((ROOT / '.release/jar-manifest.json').read_text())
with zipfile.ZipFile(main_jar) as jar:
    assert set(jar.namelist()) == set(manifest), 'Unexpected application JAR entries'
    for name, digest in manifest.items():
        assert hashlib.sha256(jar.read(name)).hexdigest() == digest, 'Application entry mismatch: ' + name
    assert b'0.1.0-8' in jar.read('app/BuildInfo.class')
(app / 'BUILD-INFO.txt').write_text('Music Manga 0.1.0-8\nPrivate source commit: f8073b2fdbe6e344677f64554a3d28afcb0fec1e\nCompiled with Kotlin 2.3.21 / JDK 21. Validated with 130 tests, including secure-session and UI regressions.\n')
for file in app.rglob('*'):
    assert not any(part in {'.git', '.aws', '.config', '.ssh', '.runtime'} for part in file.parts)
    assert not file.name.lower().endswith(('.db', '.sqlite', '.keystore', '.jks', '.pem', '.log'))
tar = OUT / f'music-manga-{VERSION}-linux-x64.tar.gz'
subprocess.run(['tar', '--sort=name', '--mtime=@0', '--owner=0', '--group=0', '--numeric-owner', '-czf', str(tar), '-C', str(WORK), 'music-manga'], check=True)
package = WORK / 'package'
(package / 'opt').mkdir(parents=True)
shutil.copytree(app, package / 'opt/music-manga', symlinks=True)
(package / 'usr/bin').mkdir(parents=True)
(package / 'usr/bin/music-manga').symlink_to('/opt/music-manga/bin/music-manga')
apps = package / 'usr/share/applications'
apps.mkdir(parents=True)
(apps / 'music-manga.desktop').write_text('[Desktop Entry]\nName=Music Manga\nComment=Music, Manga & Audiobook client\nExec=/opt/music-manga/bin/music-manga\nIcon=music-manga\nTerminal=false\nType=Application\nCategories=AudioVideo;Audio;Player;Viewer;\nStartupWMClass=app-MainKt\n')
icon = package / 'usr/share/icons/hicolor/512x512/apps/music-manga.png'
icon.parent.mkdir(parents=True)
shutil.copy(app / 'lib/music-manga.png', icon)
control = WORK / 'deb-control'
control.mkdir()
(control / 'control').write_text(f'Package: music-manga\nVersion: {VERSION}\nSection: sound\nPriority: optional\nArchitecture: amd64\nDepends: libmpv2 | libmpv1, libsecret-1-0\nMaintainer: xHitech\nDescription: Music, Manga and Audiobook client for personal libraries\n')
(control / 'debian-binary').write_text('2.0\n')
subprocess.run(['tar', '--owner=0', '--group=0', '--numeric-owner', '-czf', str(control / 'control.tar.gz'), '-C', str(control), './control'], check=True)
subprocess.run(['tar', '--owner=0', '--group=0', '--numeric-owner', '-czf', str(control / 'data.tar.gz'), '-C', str(package), '.'], check=True)
subprocess.run(['ar', 'rcs', str(OUT / f'music-manga_{VERSION}_amd64.deb'), str(control / 'debian-binary'), str(control / 'control.tar.gz'), str(control / 'data.tar.gz')], check=True)
size = sum(p.stat().st_size for p in package.rglob('*') if p.is_file())
(package / '.PKGINFO').write_text(f'pkgname = music-manga-bin\npkgbase = music-manga-bin\npkgver = {VERSION}\npkgdesc = Music, Manga and Audiobook client with embedded JRE 21\nurl = https://github.com/xHitech/music-manga-linux\nbuilddate = {int(time.time())}\npackager = xHitech\nsize = {size}\narch = x86_64\nlicense = custom\ndepend = mpv\ndepend = libsecret\noptdepend = org.freedesktop.secrets: manter a sessao no cofre do sistema\nprovides = music-manga\nconflict = music-manga\n')
archive = OUT / f'music-manga-bin-{VERSION}-x86_64.pkg.tar.zst'
with archive.open('wb') as destination:
    pipe = subprocess.Popen(['bsdtar', '--uid', '0', '--gid', '0', '--uname', 'root', '--gname', 'root', '-cf', '-', '-C', str(package), '.PKGINFO', 'opt', 'usr'], stdout=subprocess.PIPE)
    result = subprocess.run(['zstd', '-T0', '-3', '--stdout'], stdin=pipe.stdout, stdout=destination, check=True)
    pipe.stdout.close()
    assert pipe.wait() == 0
checksums = ''.join(hashlib.sha256(file.read_bytes()).hexdigest() + '  ' + file.name + '\n' for file in sorted(OUT.iterdir()) if file.is_file())
(OUT / 'SHA256SUMS.txt').write_text(checksums)
print(checksums)
print('All application JAR entries match the locally validated build. No private source checkout was used.')
