import json
import datetime
import random

# 日数
n = 1000


def create_sample_directory(parent, children, file_name):
    date = []
    infected = []
    dead = []
    tested = []
    hospitalized = []
    population = []

    # 値設定
    for i in range(n):
        date.append(str(datetime.date.today() - datetime.timedelta(days=n - i)))
        infected.append(random.randint(100, 1000))
        dead.append(random.randint(100, 500))
        tested.append(random.randint(10 ** 5, 10 ** 7))
        hospitalized.append(random.randint(10 ** 6, 10 ** 7))

    population.append(10 ** 6)

    data = {
        "date": date,
        "infected": infected,
        "dead": dead,
        "tested": tested,
        "hospitalized": hospitalized,
        "population": population,
        "parent": parent,
        "children": children
    }

    with open(file_name, 'w') as f:
        json.dump(data, f, ensure_ascii=False)


create_sample_directory(['Japan'], ['Hokkaido'], './World/Asia/Japan/Japan.json')
