import tkinter as tk
from tkinter import filedialog, simpledialog
from moviepy import VideoFileClip
import os


def get_video_size(file_path):
    """Obtém o tamanho do arquivo de vídeo em MB"""
    file_size = os.path.getsize(file_path)  # Tamanho em bytes
    return file_size / (1024 * 1024)  # Converte para MB


def calculate_ideal_size(duration, resolution="1080p"):
    """Calcula o tamanho ideal do vídeo com base no bitrate e na duração"""
    if resolution == "4K":
        bitrate_mbps = 20  # Ideal para 4K
    elif resolution == "2K":
        bitrate_mbps = 10  # Ideal para 2K
    elif resolution == "1080p":
        bitrate_mbps = 5  # Ideal para 1080p
    elif resolution == "720p":
        bitrate_mbps = 3  # Ideal para 720p
    else:
        bitrate_mbps = 1.5  # Ideal para resoluções menores

    # Converte bitrate de Mbps para MBps e multiplica pela duração
    bitrate_MBps = bitrate_mbps / 8  # 1 byte = 8 bits
    ideal_size_MB = bitrate_MBps * duration  # Tamanho ideal em MB
    return ideal_size_MB


def compress_video(input_file, output_file, target_size):
    # Carregar o vídeo
    clip = VideoFileClip(input_file)

    # Calcula a taxa de compressão necessária
    bitrate = (target_size * 8) / clip.duration  # target_size em bytes, duração em segundos

    # Exporta o vídeo comprimido
    clip.write_videofile(output_file, bitrate=f"{bitrate / 1000:.0f}k")

    print(f"Vídeo comprimido salvo em: {output_file}")


def select_file_and_compress():
    # Configuração da janela principal do tkinter
    root = tk.Tk()
    root.withdraw()  # Oculta a janela principal

    # Seleciona o arquivo de vídeo
    input_file = filedialog.askopenfilename(
        title="Selecione o vídeo que deseja comprimir",
        filetypes=[("Arquivos de vídeo", "*.mp4;*.avi;*.mov;*.mkv")]
    )

    if input_file:
        # Obtém o tamanho atual do arquivo de vídeo
        current_size_mb = get_video_size(input_file)
        print(f"Tamanho atual do vídeo: {current_size_mb:.2f} MB")

        # Obtém a duração do vídeo
        clip = VideoFileClip(input_file)
        duration = clip.duration  # em segundos

        # Calcula o tamanho ideal com base na resolução
        resolution = simpledialog.askstring(
            "Resolução", 
            "Digite a resolução do vídeo (4K, 2K, 1080p, 720p ou 480p):", 
            initialvalue="1080p"
        )
        ideal_size_mb = calculate_ideal_size(duration, resolution)

        print(f"Tamanho ideal recomendado: {ideal_size_mb:.2f} MB para manter uma boa qualidade.")

        # Solicita o tamanho desejado do vídeo comprimido em MB
        target_size_mb = simpledialog.askfloat(
            "Tamanho do Vídeo",
            f"Digite o tamanho desejado do vídeo comprimido em MB (Máximo recomendado: {current_size_mb:.2f} MB, Ideal: {ideal_size_mb:.2f} MB):"
        )

        if target_size_mb:
            # Verifica se o tamanho desejado é maior que o tamanho atual
            if target_size_mb > current_size_mb:
                print(
                    f"O tamanho solicitado ({target_size_mb} MB) é maior que o tamanho do vídeo atual ({current_size_mb:.2f} MB).")
                return

            # Define o nome de saída para o vídeo comprimido
            output_file = filedialog.asksaveasfilename(
                title="Salvar vídeo comprimido como",
                defaultextension=".mp4",
                filetypes=[("Arquivos de vídeo", "*.mp4")]
            )

            if output_file:
                # Chama a função de compressão
                compress_video(input_file, output_file, target_size_mb * 1024 * 1024)
            else:
                print("Nenhum arquivo de saída selecionado.")
        else:
            print("Nenhum tamanho de vídeo foi especificado.")
    else:
        print("Nenhum arquivo de vídeo selecionado.")


# Executa a função principal
if __name__ == "__main__":
    select_file_and_compress()
