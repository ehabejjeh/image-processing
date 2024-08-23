from PIL import Image
from pathlib import Path


def png_to_jpg():
    for filename in Path("jpgImages").iterdir():
        if filename.suffix == ".jpg":
            new_filename = filename.with_suffix(".png")
            print(new_filename)
