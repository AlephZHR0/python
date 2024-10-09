from pytube import YouTube
import os
import re

# video_url = input("Link do vídeo:")
video_url = "https://www.youtube.com/watch?v=Tuc1mCYkUZw"
output_path = "/content/drive/MyDrive/Youtube"

video = YouTube(video_url)

with open(f'teste.txt', 'w', encoding='utf-8') as f:
    f.write(video.description)

clean_title = re.sub(r'[^\w\s]', '', video.title)

video_stream = video.streams.get_highest_resolution()
video_stream.download(output_path=output_path, filename=f"{clean_title}.mp4")

# audio_stream = video.streams.get_audio_only()
# audio_stream.download(output_path=output_path, filename=f"{clean_title)}.mp3")

print("Download concluído.")