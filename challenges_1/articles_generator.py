# coding: utf-8
import urllib
import json
import random

AVAILABLE_ARTICLE_THEMES = [
    'astronomy',
    'geology',
    'gyroscope',
    'literature',
    'marketing',
    'mathematics',
    'music',
    'polit',
    'agrobiologia',
    'law',
    'psychology',
    'geography',
    'physics',
    'philosophy',
    'chemistry',
    'estetica'
]


def generate_title():
    raw_title = urllib.urlopen('https://referats.yandex.ru/creator/write/').read()
    return raw_title.decode('utf-8').capitalize()


def generate_article(themes):
    for topic in themes:
        assert topic in AVAILABLE_ARTICLE_THEMES
    url_template = 'https://referats.yandex.ru/referats/write/?%s'
    url = url_template % urllib.urlencode({'t': '+'.join(themes)})
    raw_text = urllib.urlopen(url).read().decode('utf-8')
    article = '<p>%s' % '<p>'.join(raw_text.split('<p>')[1:])
    return article


#   1. Генератор статей
#   В файле articles_generator.py есть функции generate_title и generate_article, 
#   которые генерируют заголовок и текст статьи с заданной темой при помощи Яндекс.Рефератов.
#   Нужно при помощи этих функций сгенерировать 100 статей для блога (см. задачу 6 практикума на лекции 1). 
#   На выходе - файл articles.json с сотней статей (у статьи должны быть поля title, text, author).
#   Статьи должны генерироваться при выполнении команды python articles_generator.py
def generate_full_articles(number_of_articles=10, number_of_themes=2):
    if number_of_articles < 1:
        print u'Установлено минимальное значение колличества статей = 1'
        number_of_articles = 1
    elif number_of_articles > 100:
        print u'Установлено максимальное значение колличества статей = 100'
        number_of_articles = 100

    if number_of_themes < 2:
        print u'Установлено минимальное значение number_of_themes = 2'
        number_of_themes = 2
    elif number_of_themes > 10:
        print u'Установлено максимальное значение number_of_themes = 10'
        number_of_themes = 10

    my_articles = []
    i = 0
    while i < number_of_articles:
        i += 1

        random_themes = []
        j = 0
        while j < number_of_themes:
            j += 1
            random_themes.append(random.choice(AVAILABLE_ARTICLE_THEMES))

        my_articles.append({
            'title': generate_title(),
            'text': generate_article(random_themes),
            'author': 'Superman'
        })
    json.dump(my_articles, open('articles.json', 'w'))


# 2. Пагинированный вывод статей
# Научиться выводить статьи в консоль и html-файл (как в задачах 6 и 7 практикума), но не все, а частями.
# Функция output_articles вывода должна принимать на вход способ вывода статьи (консоль/путь к файлу),
# номер страницы и количество статей на одной странице.
# Например, при выводе 6й страницы по 4 статьи должны быть выведены статьи 21-24.
def output_articles(output_type, page_number, articles_number):
    assert page_number >= 1
    articles = json.load(open('articles.json', 'r'))

    first_article_index = (page_number - 1) * articles_number
    last_article_index = first_article_index + articles_number
    if first_article_index > len(articles):
        print "В данном диапазоне нет статей"
        return
    elif last_article_index > len(articles):
        last_article_index = len(articles)
    filtered_articles = articles[first_article_index:last_article_index]

    if output_type == 'console':
        output_console(filtered_articles)
    else:
        output_file(output_type, filtered_articles)


def output_console(set_of_articles):
    for article in set_of_articles:
        print '%s\n\n%s\n\n%s(c)\n_______\n' % (article[u'title'], article[u'text'], article[u'author'])


def output_file(file_name, set_of_articles):
    with open(file_name + '.html', 'w') as f:
        for article in set_of_articles:
            string = '<h1>%s</h1>\n<div>%s</div>\n' \
                     % (article['title'].encode('utf-8'), article['text'].encode('utf-8'))
            f.write(string)


# 3. Поиск по статьям
# Реализовать функцию find_articles, которая принимает на вход поисковый запрос и список статей,
# а возвращает только те статьи, которые содержат в названии поисковый запрос.
# Опционально - добавить возможность расширенного поиска, в таком случае возвращаться будут статьи,
# в которые поисковый запросa содержится в названии или тексте.
def find_articles(query, articles_list):
    filtered_articles = []
    for article in articles_list:
        if query in article['title'].encode('utf-8'):
            filtered_articles.append(article)
    return filtered_articles


if __name__ == "__main__":
    title = generate_title()
    text = generate_article(['mathematics', 'psychology'])
    # print title
    # print text

    # YOUR CODE HERE

    generate_full_articles(24, 12)
    print '**************************************************************'

    output_articles('console', 4, 3)
    print '**************************************************************'

    output_articles('paginated_articles', 41, 3)
    print '**************************************************************'

    articles = find_articles('ика', json.load(open('articles.json', 'r')))
    for article in articles:
        print '%s\n\n%s\n\n%s(c)\n_______\n' % (article[u'title'], article[u'text'], article[u'author'])
