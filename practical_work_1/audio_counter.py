# -*- coding: utf-8 -*- 

#   2. Output audios
#
#   Создать текстовый файл audio_counter.py
#   В нём создать список аудио-записей (каждая запись - это словарь из исполнителя и названия)
#   Написать функцию, которая выводит список аудио-записей на экран
#   Вызвать эту функцию
#   Запустить скрипт (python audio_counter.py)
#   Полюбоваться правильным результатом
myAudios = [{'artist': u"Шуфутинский", 'title': u"3-е сентября"},
            {'artist': u"Чайковский", 'title': u"Адажио из балета Щелкунчик"},
            {'artist': u"ILWT", 'title': u"Все твои друзья"},
            {'artist': u"ILWT", 'title': u"Еду к бабе на Семеновскую"},
            {'artist': u"Стас Михайлов", 'title': u"Для тебя"},
            {'artist': u"Стас Михайлов", 'title': u"Без тебя"},
            {'artist': u"Стас Михайлов", 'title': u"Под тебя"},
            {'artist': u"Madrugada", 'title': u"Black Mambo"},
            {'artist': u"Tropkillaz", 'title': u"Boa Noite"}]


def print_all(audios):
    for audio in audios:
        print '%s - %s' % (audio['artist'], audio['title'])


#   3. Count audios
#
#   В файл audio_counter.py добавить функцию count_artists.
#   Функция принимает на вход список аудио (тех самых, из предыдущей задачи).
#   На выходе - словарь, в котором ключ - исполнитель, а значение - количество песен этого исполнителя в списке записей.
#   Запустить функцию, вывести результат в консоль.
def count_artists(audios, artist_name):
    a = [audio for audio in audios if audio['artist'] == artist_name]
    return {'artist': artist_name, 'number': len(a)}


#   4. Testing count audios
#
#   В audio_counter.py добавить функцию test_count_artists.
#   Функция должна проверять, что count_artists работает верно.
#   Для этого она должна запускать функцию с разными наборами аудио и проверять, что результат её работы соответствует ожидаемому.
#   Функция должна возвращать True или False в зависимости от того, верно работает функция или нет.
def test_count_artist(audios):
    a = count_artists(audios, u"Шуфутинский")
    if a['number'] != 1: return False
    a = count_artists(audios, u"Чайковский")
    if a['number'] != 1: return False
    a = count_artists(audios, u"ILWT")
    if a['number'] != 2: return False
    a = count_artists(audios, u"Стас Михайлов")
    if a['number'] != 3: return False
    a = count_artists(audios, u"Madrugada")
    if a['number'] != 1: return False
    a = count_artists(audios, u"Tropkillaz")
    if a['number'] != 1: return False
    return True


print_all(myAudios)
print test_count_artist(myAudios)
