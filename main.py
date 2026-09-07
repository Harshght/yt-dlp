from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import yt_dlp
import os

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class DownloadRequest(BaseModel):
    url: str
    is_playlist: bool
    quality: str
    download_path: str

def get_default_downloads_folder():
    user_home = os.path.expanduser('~')
    onedrive_downloads = os.path.join(user_home, 'OneDrive', 'Downloads')
    if os.path.exists(onedrive_downloads):
        return onedrive_downloads
    return os.path.join(user_home, 'Downloads')

@app.post("/download")
def download_video(req: DownloadRequest):
    if req.quality == 'best':
        format_str = 'bestvideo+bestaudio/best'
    else:
        format_str = f'bestvideo[height<={req.quality}]+bestaudio/best'

    save_path = req.download_path.strip() if req.download_path and req.download_path.strip() else get_default_downloads_folder()

    if req.is_playlist:
        outtmpl = os.path.join(save_path, '%(playlist_title)s', '%(title)s.%(ext)s')
    else:
        outtmpl = os.path.join(save_path, '%(title)s.%(ext)s')

    ydl_opts = {
        'format': format_str,
        'outtmpl': outtmpl,
        'noplaylist': not req.is_playlist,
        'merge_output_format': 'mp4',
        'overwrites': True,           # Overwrites existing files instead of skipping
        'windowsfilenames': True,     # Sanitizes special characters like $ for Windows Explorer
        'quiet': False
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([req.url])
        return {"status": "success", "message": f"Successfully downloaded to {save_path}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))