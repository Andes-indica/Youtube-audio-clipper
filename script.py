from yt_dlp import YoutubeDL
import subprocess

url = "https://youtu.be/_17rv6gs_98?si=7XRRRiKuMYPKu6MW&t=318"
start_time = "00:05:18"  # hh:mm:ss
end_time = "00:06:05"

#  Download audio
ydl_opts = {
    'format': 'bestaudio/best',
    'outtmpl': 'downloaded_audio.%(ext)s',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
}

with YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])

# Trim the specific segment
subprocess.run([
    'ffmpeg', '-i', 'downloaded_audio.mp3',
    '-ss', start_time, '-to', end_time,
    '-c', 'copy', 'output_clip.mp3'
])

print(" Extracted clip saved as output_clip.mp3")
