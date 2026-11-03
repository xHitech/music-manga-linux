[English](README.md) | [Português (Brasil)](README.pt-BR.md)

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
