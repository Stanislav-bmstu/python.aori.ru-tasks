# coding=utf-8
from operator import itemgetter

__author__ = 'stanislav.bmstu'


# history = [
# 	('https://mail.google.com/mail/u/0/#inbox',
#    '2015-10-10T03:59:32'),
# 	('https://mail.google.com/mail/u/0/#inbox/1502c8558e30d61a',
#    '2015-10-10T04:01:02'),
# 	('https://vk.com/feed',
#    '2015-10-10T09:23:32'),
# 	...
# 	]
# Вывести тройку самых посещаемых сайтов
# и дату последнего посещения каждого из них.
# На одном сайте много урлов и разные протоколы (http, https,...).

def get_history():
    history = [
        ('http://mail.google.com/mail/u/0/#inbox', '2001-10-10T03:59:32'),
        ('https://mail.google.com/mail/u/0/#inbox', '2002-10-10T04:01:02'),
        ('http://yandex.ru/', '2003-10-10T09:23:32'),
        ('https://vk.com/feed', '2004-10-10T09:23:32'),
        ('http://python.com/feed', '2005-10-10T09:23:32'),
        ('https://vk.com/feed', '2006-10-10T09:23:32'),
        ('http://yandex.ru/jdsfjs;adf', '2007-10-10T09:23:32'),
        ('https://python.com/feed', '2006-11-10T09:23:32'),
        ('http://python.com/feed', '2010-11-10T09:23:32'),
        ('https://vk.com/feed', '2000-12-10T09:23:32'),
        ('http://vk.com/feed', '2005-03-10T09:23:32'),
        ('https://mail.google.com/mail/u/0/#inbox', '2003-10-10T04:01:02'),
        ('https://mail.google.com/mail/u/0/#inbox', '2001-11-10T04:01:02'),
        ('http://mail.google.com/mail/u/0/#inbox', '2011-10-10T04:01:02'),
        ('http://mail.google.com/mail/u/0/#inbox', '2015-11-10T04:01:02'),
        ('https://yandex.ru/', '2015-10-10T09:23:32')
    ]
    return history


def get_top_sites(history, number_of_sites=3):
    sites_rating = {}
    sites_timestamp = {}
    for element in history:
        start_position = element[0].find('//') + 2
        end_position = element[0].find('/', start_position)
        site = element[0][start_position:end_position]
        if site in sites_rating:
            sites_rating[site] += 1
        else:
            sites_rating[site] = 1
        if site in sites_timestamp:
            if sites_timestamp[site] < element[1]:
                sites_timestamp[site] = element[1]
        else:
            sites_timestamp[site] = element[1]

    sites_top = get_sorted_top_sites(sites_rating, sites_timestamp)

    if number_of_sites > len(sites_top):
        number_of_sites = len(sites_top)
    if number_of_sites < 1:
        number_of_sites = 1

    output_top_sites(sites_top, number_of_sites)


def get_sorted_top_sites(sites_with_rating, sites_with_timestamp):
    sites_top = []
    for site in sites_with_rating:
        sites_top.append({
            'site': site,
            'rating': sites_with_rating[site],
            'timestamp': sites_with_timestamp[site]
        })
    return sorted(sites_top, key=itemgetter('rating'), reverse=True)


def output_top_sites(some_sites, number):
    for i in xrange(number):
        print u"Вы посещали сайт %s целых %s раз(а).\n" \
              u"\tПоследний раз %s.\n" % (
                  some_sites[i].get('site'),
                  some_sites[i].get('rating'),
                  some_sites[i].get('timestamp'))


if __name__ == "__main__":
    my_history = get_history()
    get_top_sites(my_history)
