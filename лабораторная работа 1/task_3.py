list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

# TODO Разделите участников на две команды
number_of_players = len(list_players)
middle_index = number_of_players // 2
first_team = list_players[:middle_index]
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
