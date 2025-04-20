# Compressor de Vídeo

Um aplicativo com interface gráfica para compressão de vídeos, permitindo selecionar a resolução desejada e o tamanho final em MB.

## Requisitos
- Python 3.x
- Bibliotecas: `moviepy`, `tkinter` (já incluída no Python)

## Instalação das dependências

```bash
pip install moviepy

💡 O tkinter já vem instalado com o Python em sistemas Windows. Se estiver usando Linux e não tiver, instale com: sudo apt install python3-tk

Como usar
1. Execute o script compress_video.py
2. Selecione o vídeo que deseja comprimir
3. Escolha a resolução (4K, 2K, 1080p, 720p ou 480p)
4. Defina o tamanho de saída desejado (em MB)
5. Escolha onde salvar o novo vídeo comprimido

Observações
O script estima o tamanho ideal para manter boa qualidade com base na resolução e duração do vídeo.
Suporta formatos: .mp4, .avi, .mov, .mkv
