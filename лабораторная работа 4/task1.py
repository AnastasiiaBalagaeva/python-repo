import json


def task() -> float:
    sum = 0
    with open('input.json') as file:
        data = json.load(file)
        for i in data:
            sum = i['score'] * i['weight'] + sum
    return sum


print(round(task(), 3))
