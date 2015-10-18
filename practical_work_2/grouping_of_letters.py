# coding=utf-8
__author__ = 'stanislav.bmstu'


# 1. C
#
# emails = [{'from': 'bmstu.py@gmail.com', 'title': 'Notes',
#            'important': True}, ...]
# Вывести emails в консоль с группировкой по полю from:
#
# bmstu.py@gmail.com
#   [!] Notes
# 	Какой-то спам
# 	Третье письмо
# postmaster@python.ci.aori.ru
# 	Welcome
# 	Password reset
#
# Перед важными письмами выводить восклицательный знак.
def generate_emails():
    emails = [{'from': 'bmstu.py@gmail.com', 'title': u'Notes',
               'important': True, 'text': u'Очень важный текст',
               'timestamp': '2013-10-10T03:59:32'},
              {'from': 'kate@gmail.com', 'title': u'LOST',
               'important': True, 'text': u'Очень потеря...',
               'timestamp': '2009-10-10T03:59:32'},
              {'from': 'kate@gmail.com', 'title': u'LOST',
               'important': False, 'text': u'Полетела на Oceanic Airlines. '
                                           u'Скоро буду',
               'timestamp': '2005-10-10T03:59:32'},
              {'from': 'ivan@yandex.ru', 'title': u'Гневное письмо',
               'important': False, 'text': u'Очень гневный текст',
               'timestamp': '2015-10-10T03:59:32'},
              {'from': 'maria@mail.ru', 'title': u'Новая папка',
               'important': False, 'text': u'Очень новый текст',
               'timestamp': '2011-10-10T03:59:32'},
              {'from': 'kate@gmail.com', 'title': u'LOST',
               'important': True, 'text': u'Что здесь происходит?!?!?!',
               'timestamp': '2007-10-10T03:59:32'},
              {'from': 'dude@bmstu.ru', 'title': u'Новый папка',
               'important': True, 'text': u'Очень неожиданный текст',
               'timestamp': '2015-10-10T03:59:32'},
              {'from': 'kate@gmail.com', 'title': u'LOST',
               'important': True, 'text': u'Где Джек?',
               'timestamp': '2010-10-10T03:59:32'},
              {'from': 'pavel@random.com', 'title': u'Такие дела',
               'important': False, 'text': u'Очень деловой текст',
               'timestamp': '2012-10-10T03:59:32'},
              {'from': 'liza@gmail.com', 'title': u'WTF',
               'important': False, 'text': u'Ё№;?:№*?;:(№*%"%№"',
               'timestamp': '2035-10-10T03:59:32'}]
    return emails


def output_console(emails):
    for email in emails:
        importance = "[!] " if email['important'] else ""
        print ("%s\n\t%s%s\n\t%s\n\t%s\n" %
               (email['from'], importance, email['title'],
                email['text'], email['timestamp']))


if __name__ == "__main__":
    new_emails = generate_emails()
    output_console(new_emails)
