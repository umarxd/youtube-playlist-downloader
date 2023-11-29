import sys
import yt_dlp as youtube_dl

def download_playlist(playlist_url, output_path='./downloads'):
    ydl_opts = {
        'quiet': False,
        'outtmpl': f'{output_path}/%(title)s.%(ext)s',
        'format': '18'  # Code for 360p resolution
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        ydl.download([playlist_url])

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <playlist_url> <output_path>")
        sys.exit(1)

    playlist_url = sys.argv[1]
    output_path = sys.argv[2]

    download_playlist(playlist_url, output_path)
