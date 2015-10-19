# coding=utf-8
from bottle import route, run, template
import csv
import requests
from recommend_movie import find_films, get_random_film
from parser_rating import get_rating
from bs4 import BeautifulSoup
from google import search
__author__ = 'stanislav.bmstu'


# 4. Веб-интерфейс
# Да, я знаю, о чём вы думаете. Вот уже второе ДЗ - и ни одного сайта.
# Пора это исправить.
# Надо сделать сайт, который будет являться веб-интерфейсом
# к советчику из предыдущих заданий.

# На этом сайте зайдя по ссылке /movies/drama/1995/,
# я рассчитываю увидеть рекомендуемый мне фильм (драму 95го).
# Точнее, его название, рейтинг (см. третье задание)
# и изображение (ссылку на него тоже можно стащить с IMDB).

# В качестве фреймворка (aka волшебной таблетки,
# которая поможет из скрипта сделать сайт)
# настойчиво советую использовать bottle.py.
# Там прямо по ссылке туториал, в котором есть всё, что нужно.
# Не забудьте перечислить все сторонние пакеты
# с замороженными версиями в requirements.txt.
# ADVANCED: заметили, что вытащить нужную картинку из IMDB уже не так просто?
# Для таких задач принято использовать парсеры html/xml,
# например, Beautiful Soup.

# 5. Ссылка на страницу фильма на википедии
# К картинке, названию и рейтингу теперь неплохо бы
# добавить ссылку на страницу фильма на вики -
# чтобы можно было зайти и почитать про фильм подробнее.
# Собственно, задача состоит в этом, метод решения подойдёт любой.
# Вот первый вариант, который пришёл мне в голову:
# сделать запрос в гугл "%название фильма% %год фильма% wikipedia",
# тогда первая же ссылка на википедию будет вести именно на страницу фильма.
# Для этого придётся научиться пользоваться гугловым поиском из python,
# а это не сложно, если использовать батарейку google (quickstart).


all_genres = ['unknown', 'action', 'adventure', 'animation',
              "children's", 'comedy', 'crime', 'documentary',
              'drama', 'fantasy', 'film-noir', 'horror',
              'musical', 'mystery', 'romance', 'sci-fi',
              'thriller', 'war', 'western']


def start(genre, year):
    if genre in all_genres:
        with open('movies.csv', 'rb') as csv_file:
            movie_reader = csv.reader(csv_file, delimiter='|', quotechar=' ')
            films = find_films(genre, year, movie_reader)
            random_film = get_random_film(films)

            film_title = random_film[1]
            film_rating = get_rating(random_film)
            film_imdb_url = random_film[4]

            result = {
                'film': film_title,
                'rating': film_rating,
                'url': film_imdb_url
            }
            return result


def find_image(film_info):
    imdb_html = requests.get(film_info['url']).text
    soup = BeautifulSoup(imdb_html, 'html.parser')
    imgs = soup.find_all('img')
    img_position = 2
    return str(imgs[img_position]['src'])


def get_wiki_url(film_info, year):
    film_query = "%s %s wikipedia" % (str(film_info['film']), year)
    print film_query
    search_results = []
    for url in search(film_query, stop=20):
            search_results.append(url)
    return search_results[0]


@route('/movies/<genre>/<year>')
def index(genre, year):
    film_info = start(genre, year)
    wiki_url = get_wiki_url(film_info,year)
    img_url = find_image(film_info)

    if genre in all_genres:
        return template("""
        <b>{{title}} <br>Rating: {{rating}}</b>
        <div><img height="317" width="214" src="{{img_url}}"></div>
        <a href="{{wiki_url}}">Посмотреть на wiki.</a>""",
                        title=film_info['film'],
                        rating=film_info['rating'],
                        img_url=img_url,
                        wiki_url=wiki_url)


run(host='localhost', port=8085)
