import os
import tkinter as tk
from tkinter import filedialog

# Указываем слова для удаления из имен файлов и папок
words_to_remove = ["[SW.BAND]", "[SLIV.SITE]"]

# Указываем запрещенные фразы для удаления файлов
banned_phrases = [
    "[DMC.RIP] Качай редкие курсы!",
    "[WWW.SW.BAND] 150000 курсов ждут тебя!",
    "[WWW.SW.BAND] Прочти перед изучением!",
    "Перед изучением, посмотри сюда.txt"
]

def remove_words_and_delete_files(root_dir, words_to_remove, banned_phrases):
    # Проходим по всем файлам и папкам, начиная с самого глубокого уровня
    for dirpath, dirnames, filenames in os.walk(root_dir, topdown=False):
        # Сначала обрабатываем файлы
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)

            # Проверяем на наличие запрещенных фраз
            if any(phrase in filename for phrase in banned_phrases):
                os.remove(file_path)
                print(f"Удалён файл: {file_path}")
                continue  # Переходим к следующему файлу

            # Переименовываем файл, если содержит одно из слов в words_to_remove
            new_file_name = filename
            for word in words_to_remove:
                new_file_name = new_file_name.replace(word, "")

            if new_file_name != filename:  # Проверяем, изменилось ли имя файла
                new_file_path = os.path.join(dirpath, new_file_name)
                os.rename(file_path, new_file_path)
                print(f"Переименован файл: {file_path} -> {new_file_path}")
        
        # Затем обрабатываем папки
        for dirname in dirnames:
            dir_path = os.path.join(dirpath, dirname)

            # Переименовываем папку, если содержит одно из слов в words_to_remove
            new_dir_name = dirname
            for word in words_to_remove:
                new_dir_name = new_dir_name.replace(word, "")

            if new_dir_name != dirname:  # Проверяем, изменилось ли имя папки
                new_dir_path = os.path.join(dirpath, new_dir_name)
                os.rename(dir_path, new_dir_path)
                print(f"Переименована папка: {dir_path} -> {new_dir_path}")

# Открываем диалог для выбора папки
root = tk.Tk()
root.withdraw()  # Скрываем главное окно
folder_selected = filedialog.askdirectory(title="Выберите папку для обработки")

if folder_selected:
    print(f"Выбрана папка: {folder_selected}")
    remove_words_and_delete_files(folder_selected, words_to_remove, banned_phrases)
else:
    print("Папка не выбрана.")
