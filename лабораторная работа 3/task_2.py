# TODO Напишите функцию find_common_participants
def find_common_participants(first, second, sep=','):
    first_str = set(first.split(sep))
    second_str = set(second.split(sep))
    common = first_str.intersection(second_str)
    return sorted(common)


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, sep='|'))