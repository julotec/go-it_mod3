import os #interakcja z systemem operacyjnym
import shutil #zestaw narzędzi do manipulacji plikami
from concurrent.futures import ThreadPoolExecutor

def sort_files(source_folder, destiny_folder):
    if not os.path.exists(destiny_folder): #spr czy dana ścieżka istnieje
        os.makedirs(destiny_folder) #tworzenie katalogu rekurencyjnego

    with ThreadPoolExecutor(max_workers=os.cpu_count()) as executor:
        for root, dirs, files in os.walk(source_folder):
            for file in files:
                file_path = os.path.join(root, file)
                executor.submit(move_file, file_path, destiny_folder)

def move_file(file_path, destiny_folder):
    _, ext = os.path.splitext(file_path)
    ext = ext[1:] #usunięcie kropki z rozszerzenia

    ext_folder = os.path.join(destiny_folder, ext)
    if not os.path.exists(ext_folder):
        os.makedirs(ext_folder)

    shutil.move(file_path, os.path.join(ext_folder, os.path.basename(file_path))) #przeniesienie z pliku do source do pliku destiny

if __name__ == "__main__":
    src_folder = "Bałagan"
    dsc_folder = "Sorted_File"

    sort_files(src_folder, dsc_folder)





