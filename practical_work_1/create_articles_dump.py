# -*- coding: utf-8 -*- 

#	6. Blog

#	Создать файл create_articles_dump.py.
#	Создать список статей (статья - словарь из заголовка, текста и автора).
#	Сохранить их в файл articles.json.
import json

my_articles = [{'title': u"Волк", 'text': u"Семеро козлят", 'author': u"Медведь"},
               {'title': u"Осина", 'text': u"Осиновые колья и с чем их едят", 'author': u"Дед"},
               {'title': u"Колобок", 'text': u"Проблемы выпечки шарообразной еды", 'author': u"Бабка"},
               {'title': u"Хлеб", 'text': u"Всему голова", 'author': u"Дед"}]

json.dump(my_articles, open('articles.json', 'w'))
