import yt_dlp
import os
import re
from yt_dlp.utils import DownloadError


def clean_youtube_url(url):
    """Strip tracking params and normalize Shorts URLs."""
    url = url.split('?')[0].split('&')[0]
    
    # Convert Shorts URL to standard watch URL
    shorts_match = re.search(r'youtube\.com/shorts/([a-zA-Z0-9_-]+)', url)
    if shorts_match:
        video_id = shorts_match.group(1)
        url = f"https://www.youtube.com/watch?v={video_id}"
    
    return url


def download_audio(url, output_path="outputs/audio/audio", cookies_path="cookies.txt"):
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    # Clean the URL before passing to yt-dlp
    clean_url = clean_youtube_url(url)
    if clean_url != url:
        print(f"🔗 URL normalized: {url} → {clean_url}")

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': output_path,
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'ffmpeg_location': r"C:\Users\LearnLogic\AppData\Local\Microsoft\WinGet\Packages\Gyan.FFmpeg_Microsoft.Winget.Source_8wekyb3d8bbwe\ffmpeg-8.1-full_build\bin",
        'quiet': False,
        'no_warnings': False,
        'ignoreerrors': False,
        'retries': 3,
        'socket_timeout': 30,
        # Allow Shorts and other YouTube formats
        'extractor_args': {
            'youtube': {
                'player_client': ['web', 'android'],  # try multiple clients
            }
        }
    }

    abs_cookies = os.path.abspath(cookies_path)
    if os.path.exists(abs_cookies):
        with open(abs_cookies, 'r', encoding='utf-8', errors='ignore') as f:
            first_line = f.readline().strip()
        if 'Netscape' in first_line or first_line.startswith('#'):
            ydl_opts['cookiefile'] = abs_cookies
            print(f"🍪 Using cookies from: {abs_cookies}")
        else:
            print(f"⚠️  cookies.txt is not Netscape format — skipping cookies.")
    else:
        print(f"⚠️  No cookies.txt found — proceeding without authentication.")

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(clean_url, download=True)

            if info is None:
                raise ValueError("Could not retrieve video info. The video may be private or deleted.")

            title = info.get('title', 'Unknown')
            duration = info.get('duration', 0)
            print(f"✅ Downloaded: '{title}' ({duration}s)")

    except DownloadError as e:
        print(f"\n🔴 RAW ERROR:\n{e}\n")
        error_msg = str(e).lower()

        if "not available" in error_msg or "video unavailable" in error_msg:
            raise ValueError(
                f"Video is not available. It may be private, deleted, or region-locked.\n"
                f"Original URL: {url}\n"
                f"Cleaned URL:  {clean_url}\n"
                f"Try opening the cleaned URL in a browser to confirm."
            ) from e
        elif "sign in" in error_msg or "age" in error_msg:
            raise ValueError(
                "Video requires sign-in or is age-restricted.\n"
                "Export cookies.txt from YouTube while logged in."
            ) from e
        elif "ffmpeg" in error_msg:
            raise ValueError(
                "FFmpeg not found. Check your ffmpeg_location path."
            ) from e
        elif "cookie" in error_msg:
            raise ValueError(
                "Cookie file error. Re-export cookies.txt from YouTube while logged in."
            ) from e
        else:
            raise ValueError(f"Download failed: {error_msg}") from e

    except FileNotFoundError as e:
        raise ValueError(
            "FFmpeg executable not found. Verify the ffmpeg_location path."
        ) from e

    return output_path + ".mp3"