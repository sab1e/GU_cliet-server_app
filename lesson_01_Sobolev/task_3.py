"""
3. Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе с помощью маркировки b''.

Подсказки:
--- используйте списки и циклы, не дублируйте функции
--- Попробуйте усложнить задачу, "отлавливая" и обрабатывая исключение
"""


words = [
    'attribute',
    'класс',
    'функция',
    'type',
]

for word in words:
    try:
        print(f"{word}, {type(word)}, {word.encode('ascii')}")
    except UnicodeEncodeError:
        print(f"{word}, {type(word)} - impossible encoding to bytes string")
