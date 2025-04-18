### Wallpaper Changer Script

This script changes your desktop wallpaper using a random image from Picsum. The configuration (like the wallpaper path) is stored in a `.env`.

### Setup:

1. **Create `.env` File**: 
   ```
   WALLPAPER_PATH=C:\path\to\wallpaper-changer
   ```

2. **Run Batch Script**: Create a shortcut of the batch script `wallpaper-changer.bat` then set hotkey for it using properties.

### Requirements:

- Python
- `requests` library for downloading images (`pip install requests`)