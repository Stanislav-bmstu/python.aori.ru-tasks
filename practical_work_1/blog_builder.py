# -*- coding: utf-8 -*-

#   6. Blog
#
#	Создать файл blog_builder.py, в нём загрузить список статей их файла (articles.json)
#   и читабельно вывести их в консоль.
#
#   7. Advanced blog
#
#	Вывести статьи в файл blog.html, обернув заголовок в тег h1, а текст - в тег div.
#	Открыть blog.html в браузере.
import json


def output_console(articles):
    for article in articles:
        print '%s\n\n%s\n\n %s(c)\n_______\n' % (article[u'title'], article[u'text'], article[u'author'])


def output_file(articles):
    with open('blog.html', 'w') as f:
        for article in articles:
            string = '<h1>%s</h1>\n<div>%s</div>\n' % (
                article['title'].encode('utf-8'), article['text'].encode('utf-8'))
            f.write(string)


if __name__ == "__main__":
    articles = json.load(open('articles.json', 'r'))
    output_console(articles)
    output_file(articles)
