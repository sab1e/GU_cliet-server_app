"""
1. Задание на закрепление знаний по модулю CSV. Написать скрипт,
осуществляющий выборку определенных данных из файлов info_1.txt, info_2.txt,
info_3.txt и формирующий новый «отчетный» файл в формате CSV.

Для этого:

Создать функцию get_data(), в которой в цикле осуществляется перебор файлов
с данными, их открытие и считывание данных. В этой функции из считанных данных
необходимо с помощью регулярных выражений извлечь значения параметров
«Изготовитель системы», «Название ОС», «Код продукта», «Тип системы».
Значения каждого параметра поместить в соответствующий список. Должно
получиться четыре списка — например, os_prod_list, os_name_list,
os_code_list, os_type_list. В этой же функции создать главный список
для хранения данных отчета — например, main_data — и поместить в него
названия столбцов отчета в виде списка: «Изготовитель системы»,
«Название ОС», «Код продукта», «Тип системы». Значения для этих
столбцов также оформить в виде списка и поместить в файл main_data
(также для каждого файла);

Создать функцию write_to_csv(), в которую передавать ссылку на CSV-файл.
В этой функции реализовать получение данных через вызов функции get_data(),
а также сохранение подготовленных данных в соответствующий CSV-файл;

Пример того, что должно получиться:

Изготовитель системы,Название ОС,Код продукта,Тип системы

1,LENOVO,Windows 7,00971-OEM-1982661-00231,x64-based

2,ACER,Windows 10,00971-OEM-1982661-00231,x64-based

3,DELL,Windows 8.1,00971-OEM-1982661-00231,x86-based

Обязательно проверьте, что у вас получается примерно то же самое.

ПРОШУ ВАС НЕ УДАЛЯТЬ СЛУЖЕБНЫЕ ФАЙЛЫ TXT И ИТОГОВЫЙ ФАЙЛ CSV!!!
"""
import csv
import re
from chardet import detect


FILE_LIST = ['info_1.txt', 'info_2.txt', 'info_3.txt']
FILE_REPORT = 'data_report.csv'


def encoding_convert(file_name):
    """Конвертация текстового файла в utf-8"""
    with open(file_name, 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


def get_data(file_list):
    """Извлечение параметров Название ОС, Код продукта, Изготовитель системы,
    Тип системы из файлов с данными в соответствующие списки, составление
    главного списка"""
    main_data = []
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []

    headers = [
        'N',
        'Изготовитель системы',
        'Название ОС',
        'Код продукта',
        'Тип системы',
    ]

    main_data.append(headers)

    for i, file_name in enumerate(file_list):
        encoding_convert(file_name)
        with open(file_name, 'r', encoding='utf-8') as f_obj:
            content = f_obj.read()

            pattern = r'Название ОС:\s*(.*)\n(.*\n)*' \
                      r'Код продукта:\s*(.*)\n(.*\n)*' \
                      r'Изготовитель системы:\s*(.*)\n(.*\n)*' \
                      r'Тип системы:\s*(.*)\n(.*\n)*'

            match = re.search(pattern, content)
            os_prod_list.append(match[5])
            os_name_list.append(match[1])
            os_code_list.append(match[3])
            os_type_list.append(match[7])

            main_data.append([i + 1, match[5], match[1], match[3], match[7]])

    return main_data


def write_to_csv(file_list, file_report):
    """Cохранение подготовленных данных в соответствующий CSV-файл"""
    main_data = get_data(file_list)
    with open(file_report, 'w', encoding='utf-8') as f_rep:
        f_rep_writer = csv.writer(f_rep)
        f_rep_writer.writerows(main_data)


if __name__ == '__main__':
    write_to_csv(FILE_LIST, FILE_REPORT)
