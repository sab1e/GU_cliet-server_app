"""
6. Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.

Подсказки:
--- обратите внимание, что заполнять файл вы можете в любой кодировке
но отерыть нужно ИМЕННО в формате Unicode (utf-8)

например, with open('test_file.txt', encoding='utf-8') as t_f
невыполнение условия - минус балл
"""
from chardet import detect

FILE_NAME = 'task_6.txt'

WORDS = [
    'сетевое программирование',
    'сокет',
    'декоратор',
]

with open(FILE_NAME, 'w') as f:
    print(*WORDS, file=f, sep='\n')
    print(f)


def encoding_convert(file_name):
    """Конвертация текстового файла в utf-8"""
    with open(file_name, 'rb') as f_obj:
        content_bytes = f_obj.read()
    detected = detect(content_bytes)
    encoding = detected['encoding']
    content_text = content_bytes.decode(encoding)
    with open(file_name, 'w', encoding='utf-8') as f_obj:
        f_obj.write(content_text)


encoding_convert(FILE_NAME)

with open(FILE_NAME, encoding='utf-8') as f:
    for line in f:
        print(line)
