import moviepy.editor as mp
from PIL import Image

# Caminho do arquivo de vídeo
video_path = r"C:\Users\giuli\Videos\Captures\codigo.py - Aula 2 - Python PowerUp - Visual Studio Code 2025-03-01 16-40-09.mp4"
gif_path = r"C:\ProjetosGiulio\Jornada-Python\Aula 2 - Python PowerUp\output_optimized.gif"

# Carregar o vídeo
clip = mp.VideoFileClip(video_path)

# Escolher o tempo de duração do gif, exemplo 30 segundos.
clip = clip.subclip(0, min(30, clip.duration))

# Ajustar o FPS e redimensionar a largura e altura
clip = clip.set_fps(10).resize(width=640, height=320)

# Ajusar o formato de saída
clip.write_gif(gif_path, program="ffmpeg", opt="nq")

# Retornar o caminho do GIF gerado
print(f"GIF salvo em: {gif_path}")