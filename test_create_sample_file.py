import json
import datetime
import random
import os

DEBUG = False

# 日数
n = 1000

objective_structure = {
    "World": {
        "Asia": {
            "Japan": {
                "Hokkaido": {
                    "Ishikari": {}
                }
            }
        },
        "Europe": {}
    }
}


def create_sample_directory(parent, children, file_path, key):
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

    os.makedirs(file_path, exist_ok=True)

    with open(file_path + '/' + key + '.json', 'w') as f:
        json.dump(data, f, ensure_ascii=False)


def create_directory(parent, target_object, target_dict):
    children = []
    if target_object.items():
        for key, item in target_object.items():
            if DEBUG:
                print("key: " + key + "\nitem: " + str(item))
                print(parent)
                print(list(target_object[key].keys()))
                print(target_dict + '/' + key + '/' + key + '.json')
                print()
            else:
                create_sample_directory(parent, list(target_object[key].keys()),
                                        target_dict + '/' + key, key)

            copy_parent = parent[::]
            copy_parent.append(key)
            create_directory(copy_parent, item, target_dict + '/' + key)


create_directory([], objective_structure, '.')
