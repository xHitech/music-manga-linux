# 📖🎵 Music Manga — Linux Desktop Releases

Cliente Desktop nativo para **Música Lossless/Opus**, **Leitura de Mangás em Alta Resolução** e **Audiobooks**, consumindo sua biblioteca pessoal no **Jellyfin** ou **pastas locais**.

> **Nota:** Todos os pacotes Linux já vêm com o **Runtime Java 21 (JRE) embutido e otimizado** (`jlink`). Você **não** precisa instalar Java ou SDKs na sua máquina!

---

## 🚀 Instalação Rápida (1 comando — Qualquer Distro)

Rode no terminal para instalar automaticamente as dependências de áudio (`libmpv`) e o aplicativo:

```bash
curl -fsSL https://raw.githubusercontent.com/xHitech/music-manga-linux/main/install.sh | bash
```

---

## 📦 Instalação por Distro

### 🐧 Ubuntu / Debian / Linux Mint / Pop!_OS / Zorin (`.deb`)

Baixe e instale o pacote `.deb` oficial da [última Release](https://github.com/xHitech/music-manga-linux/releases/latest):

```bash
curl -fLO https://github.com/xHitech/music-manga-linux/releases/latest/download/music-manga_0.1.0-1_amd64.deb
sudo apt update && sudo apt install -y ./music-manga_0.1.0-1_amd64.deb
```

Depois é só abrir **Music Manga** pelo menu de aplicativos ou rodando `music-manga` no terminal.

---

### 🏹 Arch Linux / Manjaro / EndeavourOS / CachyOS (`PKGBUILD` ou Portátil)

#### Opção A: Via `makepkg` (`PKGBUILD`)
```bash
git clone https://github.com/xHitech/music-manga-linux.git
cd music-manga-linux/arch
makepkg -si
```

#### Opção B: Instalação direta (Pacman + Tarball Portátil)
```bash
sudo pacman -S --needed mpv libsecret
curl -fL https://github.com/xHitech/music-manga-linux/releases/latest/download/music-manga-0.1.0-linux-x64.tar.gz | tar -xz
./music-manga/bin/music-manga
```

---

### 📁 Versão Portátil Universal (`.tar.gz`)

Funciona em qualquer distribuição Linux `x86_64` (Fedora, openSUSE, Arch, Debian, Ubuntu, Void, NixOS, etc.).

1. Certifique-se de ter a `libmpv` instalada no sistema:
   - **Arch:** `sudo pacman -S mpv libsecret`
   - **Ubuntu/Debian:** `sudo apt install libmpv2 libsecret-1-0`
   - **Fedora:** `sudo dnf install mpv-libs libsecret`
2. Baixe e extraia o arquivo [`music-manga-0.1.0-linux-x64.tar.gz`](https://github.com/xHitech/music-manga-linux/releases/latest):
   ```bash
   tar -xzf music-manga-0.1.0-linux-x64.tar.gz
   ./music-manga/bin/music-manga
   ```

---

## ✨ Principais Recursos (v0.1.0 — Manga Reader Premium 3D)

### 📖 Leitor de Mangá Premium
- **Fontes:** Bibliotecas locais (`.cbz`, `.zip` ou pastas de imagens) e bibliotecas remotas do **Jellyfin** (streaming direto de páginas dentro de arquivos `.cbz` via HTTP Range sem precisar baixar o volume inteiro antes!).
- **Renderização Adaptativa por Tiles (3B):** Zoom fluido de até 5x com decodificação regional sob demanda em alta resolução (512×512 tiles) e orçamento estrito de memória RAM.
- **Modos de Leitura (3A):** Página Simples, Página Dupla Inteligente (detecta páginas duplas/spreads largos automaticamente e isola a capa) e Rolagem Vertical Contínua (Webtoon), em sentido Oriental (Direita → Esquerda) ou Ocidental (Esquerda → Direita).
- **Laboratório de Imagem (3C/3D):** Ajustes em tempo real de **Contraste, Brilho, Saturação (Rec. 709), Ganho RGB e Curva Gamma (LUT)**, além de presets prontos (*Original, P&B Alto Contraste, P&B Suave, Leitura Noturna*) e botão **"Segure para Comparar"** (ou segure a tecla `C` / `O`).
- **Atalhos de Teclado:**
  - `Setas` / `A` / `D` / `PageUp` / `PageDown` / `Scroll`: Navegar páginas
  - `Z` ou Duplo Clique: Alternar Zoom 2.5x
  - `Ctrl + Scroll` ou `+`: Zoom progressivo no cursor
  - `R` ou `0`: Resetar Zoom
  - `C` ou `O` (segurar): Comparar com imagem original sem filtros
  - `Esc`: Voltar

### 🎵 Player de Música & Espectro Real
- **Integração Nativa `libmpv` (JNA):** Reprodução direta sem processos externos, com suporte a **Direct Play (FLAC Hi-Res / Original)** e transcoding **Opus (320 / 192 / 128 kbps)** no Jellyfin.
- **Analisador de Espectro em Memória:** Espectro de frequências real extraído diretamente do PCM em reprodução (`showfreqs` + `fscale=log`).
- **Telemetria de Stream:** Taxa de leitura de rede em tempo real, histórico dos últimos 30s e estimativa de consumo por hora.
- **Letras Sincronizadas (`.lrc`):** Destaque linha a linha sincronizado com o tempo da faixa.

### 🎧 Audiobooks
- Suporte a Audiobooks locais e remotos via Jellyfin com capítulos, retomada automática da posição exata onde parou e sincronização de sessão.

### 🔒 Segurança e Privacidade
- **Credenciais no Keyring do Sistema:** O token de sessão do Jellyfin é salvo exclusivamente via `secret-tool` (GNOME Keyring / KWallet / Secret Service) — nunca em texto puro.
- **Zero Telemetria Externa:** Nenhum dado, log ou estatística sai da sua máquina.
- **Proteção de Rede:** Bloqueio automático de redirecionamentos HTTP (`max_redirects=0`) para impedir vazamento de headers de autenticação.

---

## 🔐 Checksums (SHA-256) — v0.1.0

```text
1f5c945612c046ca963b0152750a9b879e8715bd14f3502e70be7d240f4a166c  music-manga-0.1.0-linux-x64.tar.gz
0d75e884cca8135ad8503b0dd4532992fd85c17952d3164bb8f3df31019548bd  music-manga_0.1.0-1_amd64.deb
```
