import os
from pytesseract import pytesseract
import aiopytesseract

pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
async def extract_text_async(path):
    return await aiopytesseract.image_to_string(path)

def extract_text(path):
    return pytesseract.image_to_string(path)


def get_image_paths(source_path=r'./Source/'):
    return [source_path + file for file in os.listdir(source_path) if
            file.endswith(('.png', '.jpg', '.jpeg'))]
