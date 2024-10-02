import argparse
from pathlib import Path
from shutil import copyfile
from threading import Thread
import logging

# Аргументи командного рядка
parser = argparse.ArgumentParser(description="Sorting folder")
parser.add_argument("--source", "-s", help="Source folder", required=True)
parser.add_argument("--output", "-o", help="Output folder", default="dist")

args = vars(parser.parse_args())
source = Path(args.get("source"))
output = Path(args.get("output"))

# Функція для рекурсивного обходу папок
def copy_files_in_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            # Якщо це директорія, запускаємо новий потік для її обробки
            th = Thread(target=copy_files_in_folder, args=(el,))
            th.start()
            th.join()  # Чекаємо завершення потоку для рекурсивної обробки
        elif el.is_file():
            ext = el.suffix[1:]  # Отримуємо розширення без крапки
            ext_folder = output / ext  # Директорія за розширенням
            try:
                ext_folder.mkdir(exist_ok=True, parents=True)  # Створюємо папку за розширенням
                copyfile(el, ext_folder / el.name)  # Копіюємо файл
                logging.info(f"Копіювання {el.name} до {ext_folder}")
            except OSError as err:
                logging.error(f"Помилка копіювання {el.name}: {err}")

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(threadName)s %(message)s")

    # Запускаємо обробку для джерельної папки
    copy_files_in_folder(source)

    logging.info(f"Можна видаляти {source}")
