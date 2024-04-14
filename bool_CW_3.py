import os

def get_file_size(filename):
    try:
        file_size = os.path.getsize(filename)
        return file_size
    except FileNotFoundError:
        print(f"Файл {filename} не найден.")
        return None

# Пример использования
my_file = "New"  # Замените на имя вашего файла
size_in_bytes = get_file_size(my_file)
if size_in_bytes is not None:
    print(f"Размер файла {my_file}: {size_in_bytes} байт")

