"""
3. Задание на закрепление знаний по модулю yaml.
 Написать скрипт, автоматизирующий сохранение данных
 в файле YAML-формата.
Для этого:

Подготовить данные для записи в виде словаря, в котором
первому ключу соответствует список, второму — целое число,
третьему — вложенный словарь, где значение каждого ключа —
это целое число с юникод-символом, отсутствующим в кодировке
ASCII(например, €);

Реализовать сохранение данных в файл формата YAML — например,
в файл file.yaml. При этом обеспечить стилизацию файла с помощью
параметра default_flow_style, а также установить возможность работы
с юникодом: allow_unicode = True;

Реализовать считывание данных из созданного файла и проверить,
совпадают ли они с исходными.
"""

import yaml

MAIN_DATA = {'items': ['computer', 'printer', 'keyboard', 'mouse'],
             'items_quantity': 4,
             'items_ptice': {'computer': '200€-1000€', 'keyboard': '5€-50€',
                             'mouse': '4€-7€', 'printer': '100€-300€'}}
FILE_NAME = 'file_1.yaml'


def write_to_yaml(file_name, data):
    """Запись подготовленных данных в виде словаря в файл в формате YAML"""
    with open(file_name, 'w') as f_n:
        yaml.dump(data, f_n, default_flow_style=False, allow_unicode=True)


def read_yaml(file_name):
    """Чтение данных из файла в формате YAML"""
    with open(file_name, 'r') as f_n:
        f_n_content = yaml.load(f_n, Loader=yaml.FullLoader)

    return f_n_content


if __name__ == '__main__':
    write_to_yaml(FILE_NAME, MAIN_DATA)

    if read_yaml(FILE_NAME) == MAIN_DATA:
        print('записанные данные совпадают с исходными')
    else:
        print('записанные данные не совпадают с исходными')
