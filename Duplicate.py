"""
Написать программу, которая находит и удаляет дубликаты файлов в указанной директории и всех ее поддиректориях.
"""
import os
import hashlib

def get_file_checksum(file_path):
    """
    Возвращает хеш-сумму файла.
    """
    hasher = hashlib.md5()
    with open(file_path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hasher.update(chunk)
    return hasher.hexdigest()

def find_duplicate_files(directory):
    """
    Находит дубликаты файлов в указанной директории и ее поддиректориях.
    """
    file_checksums = {}
    duplicate_files = []

    for root, _, files in os.walk(directory):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            checksum = get_file_checksum(file_path)
            if checksum in file_checksums:
                duplicate_files.append(file_path)
            else:
                file_checksums[checksum] = file_path

    return duplicate_files

def delete_duplicate_files(directory):
    """
    Удаляет дубликаты файлов в указанной директории и ее поддиректориях.
    """
    duplicate_files = find_duplicate_files(directory)

    for file_path in duplicate_files:
        os.remove(file_path)
        print(f"Удален дубликат файла: {file_path}")

    print("Удаление дубликатов завершено.")

# Пример использования:
directory_path = 'C:/Users/ge_grekov/Downloads/Тестовая'  # Замените на путь к целевой директории
delete_duplicate_files(directory_path)
