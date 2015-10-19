# coding=utf-8
import argparse
import csv
import requests
from recommend_movie import find_films, get_random_film

__author__ = 'stanislav.bmstu'


# 3. Парсер рейтинга
# В наборе данных из первой задачи есть ссылка на страницу фильма на IMDB.
# На этой странице есть рейтинг фильма.
# Задача - доработать советчик фильмов так,
# чтобы для советуемого фильма (из второй задачи)
# показывался его рейтинг.
# HINT: Если использовать модуль requests (а я рекомендую его использовать),
# то html-код страницы можно получить совсем просто:
# raw_html_text =
# requests.get('http://us.imdb.com/M/title-exact?Toy%20Story%20(1995)').text
all_genres = ['unknown', 'action', 'adventure', 'animation',
              "children's", 'comedy', 'crime', 'documentary',
              'drama', 'fantasy', 'film-noir', 'horror',
              'musical', 'mystery', 'romance', 'sci-fi',
              'thriller', 'war', 'western']


def get_rating(film):
    raw_html_text = requests.get(film[4]).text
    patern = """<div class="titlePageSprite star-box-giga-star">"""
    start_position = 49 + raw_html_text.find(patern)
    result = raw_html_text[start_position:start_position+3]
    try:
        float(result)
    except:
        result = u"Ссылка для этого фильма не актуальна."

    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--genre", help="genre")
    parser.add_argument("--year", help="year", type=int)
    args = parser.parse_args()

    genre = args.genre
    year = args.year

    if (genre is not None) & (year is not None):
        with open('movies.csv', 'rb') as csv_file:
            movie_reader = csv.reader(csv_file, delimiter='|', quotechar=' ')
            films = find_films(genre, year, movie_reader)
            random_film = get_random_film(films)
            print random_film[4]
            print get_rating(random_film)

    else:
        print(u'Слишком мало аргументов')
