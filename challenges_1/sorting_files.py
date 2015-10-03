# coding=utf-8
# 4. Сортировка файлов по размеру
# Команда `ls -lah /` показывает список файлов и каталогов в корневой директории с указанием разных параметров
# (например, прав доступа и размера файла).
# Вообще, команда `ls` умеет много всего, о всех возможностях можно почитать, выполнив `man ls`.
# Если в Python выполнить следующий код:
# import subprocess
# raw_ls_data = subprocess.check_output(['ls', '-la', '/'])
# то в переменной raw_ls_data будет строка, содержащая тот же текст,
# что выводится в результате работы `ls -la` в консоли.
# Задача: вывести список файлов (только файлов, без директорий), отсортированных по размеру.
# HINT: определителем того, является ли объект директорией, служит самый первый символ в строке.
# Для обработки строк стоит активно использовать метод split.
# Опционально: сделать путь до исследуемой директории параметром функции.
# NOTE: это учебная задача. На самом деле задача нахождения самых больших/маленьких файлов решается другими способами.
from operator import itemgetter
import subprocess


def sort_files(path):
    raw_ls_data = subprocess.check_output(['ls', '-la', path])
    data = raw_ls_data.splitlines()

    only_files_data = find_only_files_data(data)

    files = []
    for file_data in only_files_data:
        tokens = file_data.split(' ')
        tokens = [token for token in tokens if token]
        files.append({'name': tokens[8], 'size': int(tokens[4])})

    files = sorted(files, key=itemgetter('size'), reverse=True)

    sorted_files = []
    for file in files:
        print(file)
        sorted_files.append(file['name'])

    return sorted_files


def find_only_files_data(data):
    only_files_data = []
    i = 1
    while i < len(data):
        if data[i][0] == '-':
            only_files_data.append(data[i])
        i += 1
    return only_files_data


if __name__ == "__main__":
    print(sort_files('../practical_work_1/'))
