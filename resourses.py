import os

CURRENT_FILE = os.path.abspath(__file__)  # местоположение текущего файла
print(CURRENT_FILE)

CURRENT_DIR = os.path.dirname(CURRENT_FILE)  # текущая директория
print(CURRENT_DIR)

TMP_DIR = os.path.join(CURRENT_DIR, "download")  # указание директории для скачивания файла
print(TMP_DIR)