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
    biggest_bar = None
    max_seats_count = 0
    for bar in bars:
        if int(bar["SeatsCount"]) > max_seats_count:
            max_seats_count = int(bar["SeatsCount"])
            biggest_bar = bar["Name"]
    return biggest_bar


def get_smallest_bar(bars):
    smallest_bar = None
    min_seats_count = float("inf")
    for bar in bars:
        if int(bar["SeatsCount"]) < min_seats_count:
            min_seats_count = int(bar["SeatsCount"])
            smallest_bar = bar["Name"]
    return smallest_bar


def get_closest_bar(bars, longitude, latitude):
    # Принимаем, что в пределах Мщсквы поверхность Земли плоская.
    # Тогда долгота и широту можно использовать, как декартовы координаты
    closest_bar = None
    min_distance = float("inf")
    for bar in bars:
        bar_longitude, bar_latitude = bar["geoData"]["coordinates"]
        distance = math.sqrt((longitude - bar_longitude) ** 2 + (latitude - bar_latitude) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_bar = bar["Name"]
    return closest_bar


if __name__ == '__main__':
    print("Программа определяет самый большой, самый маленький и самый близкий бар.")
    while(True):
        bars_file = input("Введите имя файла с данными о барах: ")
        print("Чтение информации из файла %s ..." % bars_file)
        bars = load_data(bars_file)
        if bars is None:
            user_input = input("Прочитать данные не удалось. Повторить ввод имени файла? (y/n) ")
            if user_input.strip().lower() != "y":
                print("Выход из программы.")
                sys.exit()
        else:
            break
    print("Cамый большой бар: %s" % get_biggest_bar(bars))
    print("Cамый маленький бар: %s" % get_smallest_bar(bars))
    print("Определение ближайшего бара.")
    longitude = float(input("    Введите вашу текущую долготу: ").strip())
    latitude = float(input("    Введите вашу текущую широту: ").strip())
    print("Cамый близкий бар: %s" % get_closest_bar(bars, longitude, latitude))