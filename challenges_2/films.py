# coding=utf-8
from collections import Counter
import csv

__author__ = 'stanislav.bmstu'

# 1. Фильмы
# В файле movies.csv собрана информация о 1682х фильмах.
# Информация о фильме включает в себя его название, дату выхода,
# сылку на IMDB и принадлежность к разным жанрам.
# В этой задаче нужно узнать, в каких годах было выпущенно сколько фильмов.
# Вывести на экран год и количество фильмов из набора,
# которые вышли в этот год.
# Вот описание формата:
# movie id | movie title | release date | video release date | IMDb URL |
# unknown | Action | Adventure | Animation | Children's | Comedy | Crime |
# Documentary | Drama | Fantasy | Film-Noir | Horror | Musical | Mystery |
# Romance | Sci-Fi | Thriller | War | Western |
# IMPORTANT: если вы используете систему контроля версий,
# не надо класть movies.csv в него.
# Добавьте его в .gitignore, а в readme напишите, где он должен лежать,
# чтобы всё ожило.


def output_years_films(years):
    years_counter = Counter(years)
    for year in years_counter:
        print("В %s году было выпущено фильмов: %d"
              % (year, years_counter[year]))


if __name__ == "__main__":
    with open('movies.csv', 'rb') as csv_file:
        movie_reader = csv.reader(csv_file, delimiter='|', quotechar=' ')
        years = [row[2][-4:] for row in movie_reader]

    output_years_films(years)
