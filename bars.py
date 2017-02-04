import sys
import os
import json
import math


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath, 'r') as file_handler:
        return json.load(file_handler)


def get_biggest_bar(bars):
    return max(bars, key=lambda bar: int(bar["SeatsCount"]))


def get_smallest_bar(bars):
    return min(bars, key=lambda bar: int(bar["SeatsCount"]))


def get_closest_bar(bars, longitude, latitude):
    # Принимаем, что в пределах Мщсквы поверхность Земли плоская.
    # Тогда долгота и широту можно использовать, как декартовы координаты

    def distance(bar):
        bar_longitude, bar_latitude = bar["geoData"]["coordinates"]
        return math.sqrt((longitude - bar_longitude) ** 2 + (latitude - bar_latitude) ** 2)

    return min(bars, key=distance)


if __name__ == '__main__':
    args = sys.argv[1:]
    if not args:
        print("Usage: python bars.py filepath")
        sys.exit(2)

    bars = load_data(args[0])
    if bars is None:
        print("Прочитать данные не удалось. Выход из программы.")
        sys.exit(1)

    print("Cамый большой бар: %s" % get_biggest_bar(bars)["Name"])
    print("Cамый маленький бар: %s" % get_smallest_bar(bars)["Name"])
    print("Определение ближайшего бара.")
    longitude = float(input("    Введите вашу текущую долготу: ").strip())
    latitude = float(input("    Введите вашу текущую широту: ").strip())
    print("Cамый близкий бар: %s" % get_closest_bar(bars, longitude, latitude)["Name"])