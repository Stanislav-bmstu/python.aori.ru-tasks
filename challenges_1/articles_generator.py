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
def generate_a_hundred():
    my_articles = []
    i = 0
    while i < 100:
        i += 1
        random_theme1 = AVAILABLE_ARTICLE_THEMES[random.randint(0, 15)]
        random_theme2 = AVAILABLE_ARTICLE_THEMES[random.randint(0, 15)]
        my_articles.append({
            'title': generate_title(),
            'text': generate_article([random_theme1, random_theme2]),
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
    start = (page_number - 1) * articles_number
    end = start + articles_number
    filtered_articles = articles[start:end]
    if output_type == 'console':
        for article in filtered_articles:
            print '%s\n\n%s\n\n%s(c)\n_______\n' % (article[u'title'], article[u'text'], article[u'author'])
    else:
        with open(output_type + '.html', 'w') as f:
            for article in filtered_articles:
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
        if article['title'].encode('utf-8').find(query) != -1:
            filtered_articles.append(article)
    return filtered_articles


if __name__ == "__main__":
    title = generate_title()
    text = generate_article(['mathematics', 'psychology'])
    # print title
    # print text

    # YOUR CODE HERE

    generate_a_hundred()
    output_articles('console', 4, 3)
    output_articles('paginated_articles', 4, 3)

    articles = find_articles('ика', json.load(open('articles.json', 'r')))
    print '**************************************************************'
    for article in articles:
            print '%s\n\n%s\n\n%s(c)\n_______\n' % (article[u'title'], article[u'text'], article[u'author'])