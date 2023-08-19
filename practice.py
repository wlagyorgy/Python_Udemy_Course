import datetime
import time
import requests
from bs4 import BeautifulSoup

numbers = [12, 45, 87, 23, 56, 92, 11]

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}


def sum_avg(numbers):
    avg = sum(numbers) / len(numbers)
    return avg


def union_cut_dist(set1, set2):
    union = set1 | set2
    cut = set1.intersection(set2)
    diff1 = set1.difference(set2)
    diff2 = set2 - set1
    return union, cut, diff1, diff2


def generate_squre_numbers(n):
    squares = [x ** 2 for x in range(n)]
    return squares


def greeting():
    print("hello, what is your name?")
    name = input()
    print(f"Greetings {name}")


def write_to_file():
    f = open("even_numbers.txt", "w")
    for x in range(10):
        f.write(str(x * 2) + "\n")
    f.close()


class Car:
    def __init__(self, brand, model, speed):
        self.brand = brand
        self.model = model
        self.speed = speed

    def modify_speed(self, speed):
        self.speed = speed


def calculate_run_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        run_time = end_time - start_time
        print(f"A {func.__name__} futási ideje: {run_time} másodperc")
        return result

    return wrapper


@calculate_run_time
def slow_function():
    time.sleep(2)
    print("Lassú függvény vége.")


@calculate_run_time
def fast_function():
    print("Gyors függvény vége.")


def fibonacci_numbers(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = a, a + b


def calculate_age(birthyear):
    this_year = datetime.datetime.now().year
    print(this_year - birthyear)


def get_webpage():
    url = " https://www.index.hu"
    resp = requests.get(url)
    if resp.status_code == 200:
        soup = BeautifulSoup(resp.content, "html.parser")
        print(soup)


def get_weather(city):
    MY_API_KEY = "f9f0c0007b9190a9552320a8c7417f66"
    MY_API_KEY2 = "ee3c722a8b20297c9959b8b148ecb8e4"
    # geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={MY_API_KEY}"
    # response = requests.get(geo_url)
    # data = response.json()
    # print(data[1]["lat"])
    # lat = data[0]["lat"]
    # lon = data[1]["lon"]
    lat = 51.5073219
    lon = -0.0919983
    weather_url = f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&appid={MY_API_KEY}"
    response = requests.get(weather_url)
    data = response.json()
    print(data)
    return lat, lon


def divide_check(n1, n2):
    print(n1)
    print(n2)
    try:
        return n1 / n2
    except ZeroDivisionError:
        return "nullával osztás nem megengedett"


if __name__ == "__main__":
    # u, c, d1, d2 = union_cut_dist(set1, set2)
    # print(u, c, d1, d2)
    # print(set1, set2)
    # squares = generate_squre_numbers(10)
    # print(squares)
    # # greeting()
    # write_to_file()
    # c = Car("Tesla", "s30", 450)
    # print(c.speed)
    # print(type(c.speed))
    # c.modify_speed("300")
    # print(c.speed)
    # print(type(c.speed))
    # # slow_function()
    # # fast_function()
    fib = list(fibonacci_numbers(1))
    print(fib)
    # calculate_age(1993)
    # get_webpage()
    la, lo = get_weather("London")
    print(la, lo)
    print("adj meg 2 számot")
    number1 = int(input())
    number2 = int(input())
    print(divide_check(number1, number2))
