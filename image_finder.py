from pathlib import Path

current_dir = Path(__file__).resolve().parent

def find_image_files():
    files = [f.name for f in current_dir.iterdir() if f.is_file()]
    only_photos = []
    for f in files:
        if f.endswith(".jpg" or ".png" or ".bmp" or ".webp"):
            only_photos.append(f)
    if only_photos == []:
        return None
    else:
        return only_photos
