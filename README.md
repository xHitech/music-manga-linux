# Music Manga para Linux

O Music Manga é um aplicativo para Linux que reúne reprodução de músicas, leitura de mangás e audiobooks. Ele acessa bibliotecas pessoais do Jellyfin e arquivos locais.

Os pacotes Linux incluem o runtime Java 21. Não é necessário instalar Java separadamente.

## Instalação

Baixe o pacote adequado à sua distribuição na [página da versão mais recente](https://github.com/xHitech/music-manga-linux/releases/latest).

### Debian, Ubuntu, Linux Mint, Pop!_OS e Zorin

Baixe o pacote `.deb` na página da versão mais recente e instale-o:

```bash
sudo apt install ./music-manga_VERSION_amd64.deb
```

Substitua o nome de exemplo pelo nome do arquivo baixado. Você também pode abrir o pacote pelo gerenciador de arquivos.

### Arch Linux, Manjaro, EndeavourOS e CachyOS

Para compilar e instalar o pacote a partir do repositório:

```bash
git clone https://github.com/xHitech/music-manga-linux.git
cd music-manga-linux/arch
makepkg -si
```

Como alternativa, baixe o pacote pronto para Arch na página da versão mais recente e instale-o:

```bash
sudo pacman -U ./music-manga-bin-VERSION-x86_64.pkg.tar.zst
```

### Outras distribuições Linux

Baixe o arquivo portátil `.tar.gz` na página da versão mais recente e extraia-o:

```bash
tar -xzf music-manga-VERSION-linux-x64.tar.gz
./music-manga/bin/music-manga
```

O arquivo portátil depende da biblioteca de áudio `libmpv` do sistema. Instale-a pelo gerenciador de pacotes da sua distribuição caso o aplicativo não a encontre. Os nomes mais comuns são `mpv` no Arch, `libmpv2` no Debian ou Ubuntu e `mpv-libs` no Fedora.

Para manter a sessão do Jellyfin entre execuções, também são necessários `libsecret` e um provedor Secret Service, como GNOME Keyring ou KWallet.

## Primeiro acesso

1. Abra o Music Manga pelo menu de aplicativos ou execute `music-manga` no terminal.
2. Informe o endereço do servidor Jellyfin e os dados da sua conta.
3. Selecione as bibliotecas que deseja usar.

Também é possível acessar arquivos locais. Para mangás, o leitor aceita arquivos CBZ e ZIP e pastas com imagens.

Para manter a sessão do Jellyfin depois de fechar o aplicativo, marque **Manter sessão neste aparelho** na tela de login. O aplicativo guarda o token da sessão no cofre de credenciais do sistema; a senha não é salva. O provedor Secret Service precisa estar instalado e desbloqueado. Sem ele, a sessão será temporária.

## Recursos

### Música

- Reproduz músicas do Jellyfin, incluindo Direct Play quando permitido pelo servidor.
- Permite escolher a qualidade de transcodificação Opus quando necessária.
- Exibe letras LRC sincronizadas.
- Mostra um espectro de áudio e informações sobre o fluxo de rede.

### Mangás

- Lê arquivos CBZ e ZIP, pastas de imagens e bibliotecas compatíveis no Jellyfin.
- Abre páginas de arquivos CBZ remotos sem baixar o volume inteiro antes.
- Oferece leitura em página simples, página dupla ou rolagem vertical.
- Permite escolher o sentido de leitura, da direita para a esquerda ou da esquerda para a direita.
- Oferece zoom e ajustes de imagem durante a leitura.

### Audiobooks

- Reproduz audiobooks locais ou do Jellyfin.
- Permite navegar por capítulos e retomar a reprodução do ponto anterior.

## Privacidade

O Music Manga não envia dados de uso ou telemetria a serviços externos. Quando a opção de manter sessão está ativa, as credenciais do Jellyfin são armazenadas no cofre de credenciais do sistema.

## Versões e checksums

Os downloads e checksums SHA-256 estão na [página de versões](https://github.com/xHitech/music-manga-linux/releases). Consulte as notas de cada versão para ver mudanças e requisitos específicos.

<details>
<summary>English</summary>

# Music Manga for Linux

Music Manga is a desktop client for your personal Jellyfin server and local media libraries. It combines music playback, manga reading, and audiobook support in one Linux application.

The Linux releases include a Java 21 runtime. You do not need to install Java separately.

## Install

Download the package for your distribution from [the latest release](https://github.com/xHitech/music-manga-linux/releases/latest).

### Debian, Ubuntu, Linux Mint, Pop!_OS, and Zorin

Download the `.deb` package from the latest release, then install it:

```bash
sudo apt install ./music-manga_VERSION_amd64.deb
```

Replace the filename with the one you downloaded. You can also use your file manager to open and install the package.

### Arch Linux, Manjaro, EndeavourOS, and CachyOS

To build and install the package from the repository:

```bash
git clone https://github.com/xHitech/music-manga-linux.git
cd music-manga-linux/arch
makepkg -si
```

Alternatively, download the prebuilt Arch package from the latest release and install it with:

```bash
sudo pacman -U ./music-manga-bin-VERSION-x86_64.pkg.tar.zst
```

### Other Linux distributions

Download the portable `.tar.gz` archive from the latest release and extract it:

```bash
tar -xzf music-manga-VERSION-linux-x64.tar.gz
./music-manga/bin/music-manga
```

The portable archive requires the system audio library `libmpv`. Install it using your distribution's package manager if the application cannot find it. Common package names include `mpv` on Arch, `libmpv2` on Debian or Ubuntu, and `mpv-libs` on Fedora. The `libsecret` library and a Secret Service provider are needed to save a Jellyfin session between launches.

## First launch

1. Open Music Manga from your desktop application menu, or run `music-manga` in a terminal.
2. Enter your Jellyfin server address and account details.
3. Select the libraries you want to use.

You can also browse supported local media. For manga, the reader supports CBZ and ZIP archives and folders of images.

To keep your Jellyfin session after closing the app, select **Keep session on this device** on the login screen. The application stores the session token in the system credential store; it does not save your password. A Secret Service provider, such as GNOME Keyring or KWallet, must be installed and unlocked. Without one, the session is temporary.

## Features

### Music

- Stream music from Jellyfin, including direct playback when supported by the server.
- Choose Opus transcoding quality when transcoding is needed.
- View synchronized LRC lyrics.
- See a live audio spectrum and network stream information.

### Manga

- Read local CBZ and ZIP archives, image folders, and supported manga libraries on Jellyfin.
- Open pages from remote CBZ archives without downloading the entire volume first.
- Use single-page, double-page, and continuous vertical reading modes.
- Read from right to left or left to right.
- Zoom and adjust image appearance while reading.

### Audiobooks

- Play local or Jellyfin audiobooks.
- Navigate chapters and resume from the previous playback position.

## Privacy

Music Manga does not send usage analytics or telemetry to external services. Jellyfin credentials are handled through the system credential store when session persistence is enabled.

## Releases and checksums

Downloads and SHA-256 checksums are available on the [releases page](https://github.com/xHitech/music-manga-linux/releases). Check the release notes for version-specific changes and installation requirements.

</details>
