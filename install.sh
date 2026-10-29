#!/usr/bin/env bash
set -euo pipefail

VERSION="0.1.0-8"
REPO="xHitech/music-manga-linux"
TAR_URL="https://github.com/${REPO}/releases/download/v${VERSION}/music-manga-${VERSION}-linux-x64.tar.gz"
DEB_URL="https://github.com/${REPO}/releases/download/v${VERSION}/music-manga_${VERSION}_amd64.deb"

echo "========================================================"
echo "  Music Manga v${VERSION} — Instalador Linux (x86_64)"
echo "========================================================"

# 1. Instalar dependências nativas de sistema (libmpv + libsecret)
if command -v pacman >/dev/null 2>&1; then
    echo "[1/3] Detectado Arch Linux / derivado. Verificando dependências (mpv, libsecret)..."
    sudo pacman -S --needed --noconfirm mpv libsecret
elif command -v apt-get >/dev/null 2>&1; then
    echo "[1/3] Detectado Debian / Ubuntu / Mint / Pop!_OS. Baixando pacote .deb..."
    DOWNLOAD_DIR=$(mktemp -d)
    trap 'rm -rf -- "$DOWNLOAD_DIR"' EXIT
    TMP_DEB="$DOWNLOAD_DIR/music-manga_${VERSION}_amd64.deb"
    curl -fSL "$DEB_URL" -o "$TMP_DEB"
    echo "[2/3] Instalando pacote .deb e dependências..."
    sudo apt-get update -qq
    sudo apt-get install -y "$TMP_DEB"
    rm -f "$TMP_DEB"
    echo "[3/3] Instalação concluída! Procure por 'Music Manga' no menu de aplicativos ou digite: music-manga"
    echo " -> Para manter o login, é necessário um cofre Secret Service disponível e desbloqueado (GNOME Keyring, KWallet ou compatível)."
    exit 0
elif command -v dnf >/dev/null 2>&1; then
    echo "[1/3] Detectado Fedora / RHEL. Verificando dependências (mpv-libs, libsecret)..."
    sudo dnf install -y mpv-libs libsecret
fi

# 2. Instalação via tarball autossuficiente em ~/.local/opt/music-manga (não exige root para os binários)
INSTALL_DIR="${HOME}/.local/opt/music-manga"
BIN_DIR="${HOME}/.local/bin"
APP_DIR="${HOME}/.local/share/applications"
ICON_DIR="${HOME}/.local/share/icons/hicolor/512x512/apps"

echo "[2/3] Baixando Music Manga v${VERSION} (runtime Java 21 já incluso)..."
mkdir -p "${HOME}/.local/opt" "$BIN_DIR" "$APP_DIR" "$ICON_DIR"
DOWNLOAD_DIR=$(mktemp -d "${HOME}/.local/opt/.music-manga-install.XXXXXX")
trap 'rm -rf -- "$DOWNLOAD_DIR"' EXIT
TMP_TAR="$DOWNLOAD_DIR/music-manga-${VERSION}-linux-x64.tar.gz"
curl -fSL "$TAR_URL" -o "$TMP_TAR"

tar -xzf "$TMP_TAR" -C "$DOWNLOAD_DIR"
test -x "$DOWNLOAD_DIR/music-manga/bin/music-manga"
test -f "$DOWNLOAD_DIR/music-manga/lib/music-manga.png"
# Validate the downloaded app before replacing the existing installation.
rm -rf -- "$INSTALL_DIR"
mv -- "$DOWNLOAD_DIR/music-manga" "$INSTALL_DIR"

ln -sf "${INSTALL_DIR}/bin/music-manga" "${BIN_DIR}/music-manga"
cp "${INSTALL_DIR}/lib/music-manga.png" "${ICON_DIR}/music-manga.png"

cat << EOF > "${APP_DIR}/music-manga.desktop"
[Desktop Entry]
Name=Music Manga
Comment=Music, Manga & Audiobook Desktop Client for Jellyfin and Local Libraries
Exec=${INSTALL_DIR}/bin/music-manga
Icon=music-manga
Terminal=false
Type=Application
Categories=AudioVideo;Audio;Player;Viewer;
StartupWMClass=app-MainKt
EOF

echo "[3/3] Music Manga v${VERSION} instalado com sucesso!"
echo " -> Abra pelo menu de aplicativos ('Music Manga') ou execute:"
echo "    ${BIN_DIR}/music-manga"

echo " -> Para manter o login, é necessário um cofre Secret Service disponível e desbloqueado (GNOME Keyring, KWallet ou compatível)."
