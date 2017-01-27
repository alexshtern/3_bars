import json
import math


def load_data(filepath):
    with open(filepath, 'r') as fp:
        data = json.load(fp)
    return data


def get_biggest_bar(data):
    biggest_bar = None
    max_seats_count = 0
    for bar in data:
        if int(bar["SeatsCount"]) > max_seats_count:
            max_seats_count = int(bar["SeatsCount"])
            biggest_bar = bar["Name"]
    return biggest_bar


def get_smallest_bar(data):
    smallest_bar = None
    min_seats_count = float("inf")
    for bar in data:
        if int(bar["SeatsCount"]) < min_seats_count:
            min_seats_count = int(bar["SeatsCount"])
            smallest_bar = bar["Name"]
    return smallest_bar


def get_closest_bar(data, longitude, latitude):
    # Принимаем, что в пределах Мщсквы поверхность Земли плоская.
    # Тогда долгота и широту можно использовать, как декартовы координаты
    closest_bar = None
    min_distance = float("inf")
    for bar in data:
        bar_longitude, bar_latitude = bar["geoData"]["coordinates"]
        distance = math.sqrt((longitude - bar_longitude) ** 2 + (latitude - bar_latitude) ** 2)
        if distance < min_distance:
            min_distance = distance
            closest_bar = bar["Name"]
    return closest_bar


if __name__ == '__main__':
    bars = load_data("../data-2897-2016-11-23.json")
    print("Cамый большой бар: %s" % get_biggest_bar(bars))
    print("Cамый маленький бар: %s" % get_smallest_bar(bars))
    longitude = float(input("Долгота: ").strip())
    latitude = float(input("Широта: ").strip())
    # print("Cамый близкий бар: %s" % get_closest_bar(bars, 37.62158794615201, 55.76536695660836))
    print("Cамый близкий бар: %s" % get_closest_bar(bars, longitude, latitude))