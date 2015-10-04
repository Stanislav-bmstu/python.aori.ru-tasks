# coding=utf-8
# 6. Исследование данных
# В файле technical_education_moscow.json содержится данные
# о учебных заведениях Москвы научно-технического направления
# (данные взяты с http://data.mos.ru/).
# Для каждого заведения известны несколько параметров,
# в том числе район города, в котором это заведение находится.
# Нужно вывести пятёрку районов, в которых больше всего учебных заведений.
import json
from operator import itemgetter


def get_top_regions(number_of_top_regions=5):
    areas = {}
    all_info = json.load(open('technical_education_moscow.json', 'r'))
    for info in all_info:
        if areas.get(info['Cells']['rayon']) is not None:
            areas[info['Cells']['rayon']] += 1
        else:
            areas[info['Cells']['rayon']] = 1

    districts = []
    for area in areas:
        districts.append({'area': area, 'number': areas.get(area)})

    districts = sorted(districts, key=itemgetter('number'), reverse=True)
    if number_of_top_regions > len(districts):
        number_of_top_regions = len(districts)
    elif number_of_top_regions < 1:
        number_of_top_regions = 1

    output_regions(districts, number_of_top_regions)


def output_regions(regions, number):
    for i in xrange(number):
        print regions[i].get('area') + " : " + str(regions[i].get('number'))


if __name__ == "__main__":
    get_top_regions(5)
