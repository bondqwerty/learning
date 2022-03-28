#памятка СПИСКИ, КОРТЕЖИ, МНОЖЕСТВА, СЛОВАРИ

Списки (list), Кортежи (tuple), Множества (set и frozenset), Словари (dict)

СПИСОК lst = [1, "абв", 3, 4, 5, 6]
Командой print(lst) выводится, как: [1, 'абв', 3, 4, 5, 6]
print(type(lst): <class 'list'>

КОРТЕЖ lst = (1, "абв", 3, 4, 5, 6)
Командой print(lst) выводится, как: (1, 'абв', 3, 4, 5, 6)
print(type(lst): <class 'tuple'>
ПРИМЕЧАНИЕ: кортеж защищен от изменений его элементов, например команда lst[2] = 'ТРИ' в отличии от списка вызовет ошибку

МНОЖЕСТВО lst = {1, "абв", 3, 4, 5, 6}
Командой print(lst) выводится, как: {1, 3, 4, 5, 6, 'абв'}
print(type(lst): <class 'set'>
ПРИМЕЧАНИЕ: Множество в python - 'контейнер', содержащий не повторяющиеся элементы в случайном порядке

СЛОВАРЬ lst = {"ключ": "объект", 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
Командой print(lst) выводится, как: {'ключ': 'объект', 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
print(type(lst): <class 'dict'>
ПРИМЕЧАНИЕ: Словари в python - неупорядоченные коллекции произвольных объектов с доступом по ключу.
dictionary = {(1, 2.0): 'кортежи могут быть ключами', 1: 'целые числа могут быть ключами', 'бежать': 'строки тоже', ['носок', 1, 2.0]: 'а списки не могут'}
      
      
print('\n\tпамятка СПИСКИ, КОРТЕЖИ, МНОЖЕСТВА, СЛОВАРИ', end="\n\n")
print('\tСПИСОК lst = [1, "абв", 3, 4, 5, 6]')
lst = [1, "абв", 3, 4, 5, 6]
print("Командой print(lst) выводится, как:", lst)
print("print(type(lst):", type(lst), end="\n\n")

print('\tКОРТЕЖ lst = (1, "абв", 3, 4, 5, 6)')
lst = (1, "абв", 3, 4, 5, 6)
print("Командой print(lst) выводится, как:", lst)
print("print(type(lst):", type(lst))
print(
    "ПРИМЕЧАНИЕ: кортеж защищен от изменений его элементов,\n например команда lst[2] = 'ТРИ' в отличии от списка вызовет ошибку",
    end="\n\n")

print('\tМНОЖЕСТВО lst = {1, "абв", 3, 4, 5, 6}')
lst = {1, "абв", 3, 4, 5, 6}
print("Командой print(lst) выводится, как:", lst)
print("print(type(lst):", type(lst))
print(
    "ПРИМЕЧАНИЕ: Множество в python - 'контейнер', содержащий не повторяющиеся элементы в случайном порядке",
    end="\n\n")

print('\tСЛОВАРЬ lst = {"ключ": "объект", 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}')
lst = {"ключ": "объект", 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
print("Командой print(lst) выводится, как:", lst)
print("print(type(lst):", type(lst))
print("ПРИМЕЧАНИЕ: Словари в python - неупорядоченные коллекции произвольных объектов с доступом по ключу.\ndictionary = {(1, 2.0): 'кортежи могут быть ключами', 1: 'целые числа могут быть ключами', 'бежать': 'строки тоже', ['носок', 1, 2.0]: 'а списки не могут'}")
dictionary = {(1, 2.0): 'кортежи могут быть ключами', 1: 'целые числа могут быть ключами', 'бежать': 'строки тоже', 'носок': 'а списки не могут'}
print(dictionary)
