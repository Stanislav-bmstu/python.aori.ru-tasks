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


def research():
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

    i = 0
    while i < 5:
        print districts[i].get('area') + " : " + str(districts[i].get('number'))
        i += 1


if __name__ == "__main__":
    research()
