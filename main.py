import os
import ctypes
import requests
from datetime import datetime

WALLPAPER_DIR = os.path.join(os.getcwd(), "wallpapers")
os.makedirs(WALLPAPER_DIR, exist_ok=True)

LOREM_PICSUM_URL = "https://picsum.photos/1920/1080"

def download_wallpaper():
    try:
        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        image_name = f"wallpaper_{timestamp}.jpg"
        image_path = os.path.join(WALLPAPER_DIR, image_name)

        response = requests.get(LOREM_PICSUM_URL, timeout=15)
        if response.status_code == 200:
            with open(image_path, 'wb') as f:
                f.write(response.content)
            return image_path
        else:
            print(f"Failed to fetch image, status code: {response.status_code}")
    except Exception as e:
        print(f"Failed to download: {e}")
    return None

def set_wallpaper(image_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, image_path, 3)

def main():
    image_path = download_wallpaper()
    if image_path:
        set_wallpaper(image_path)
        print(f"Wallpaper set: {os.path.basename(image_path)}")
    else:
        print("Could not set wallpaper.")

if __name__ == "__main__":
    main()
