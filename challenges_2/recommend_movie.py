# coding=utf-8
import argparse
import csv
import random

__author__ = 'stanislav.bmstu'


# 2. Советчик фильмов
# На основании того же набора данных, что и в предыдушем задании,
# написать скрипт, который принимает на вход год и жанр,
# а выдаёт количество фильмов, которые вышли в заданном году
# и имеют заданный жанр.
# Помимо этого скрипт должен выводить название случайного фильма,
# удовлетворяющего этим критериям.
# Формат запуска скрипта из консоли должен быть следующим:
# python recommend_movie.py --genre comedy --year 1996
#
# HINT: для парсинга аргументов, с которыми запцщен скрипт
# можно использовать модуль argparse.
all_genres = ['unknown', 'action', 'adventure', 'animation',
              "children's", 'comedy', 'crime', 'documentary',
              'drama', 'fantasy', 'film-noir', 'horror',
              'musical', 'mystery', 'romance', 'sci-fi',
              'thriller', 'war', 'western']


def find_films(genre, year, movie_reader):
    col = 5 + all_genres.index(str(genre).lower())
    filtered_films = []
    for row in movie_reader:
        if (row[2][-4:] == str(year)) and (row[col] == '1'):
            filtered_films.append(row)
    return filtered_films


def output_count_films(genre, year, films):
    print(u"В %s-м году вышло %d фильмов жанра \"%s\"." %
          (year, len(films), str(genre)))


def get_random_film(films):
    return random.choice(films)


def output_film(film):
    print film[1]


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
            output_count_films(genre, year, films)
            random_film = get_random_film(films)
            output_film(random_film)
    else:
        print(u'Слишком мало аргументов')
