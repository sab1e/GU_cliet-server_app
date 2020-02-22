"""
4. Преобразовать слова «разработка», «администрирование», «protocol»,
«standard» из строкового представления в байтовое и выполнить
обратное преобразование (используя методы encode и decode).

Подсказки:
--- используйте списки и циклы, не дублируйте функции
"""


words = [
    'разработка',
    'администрирование',
    'protocol',
    'standard',
]

for word in words:
    enc_word = word.encode('utf-8')
    print(f'Байтовое представление:\n {enc_word}\n {type(enc_word)}')

    dec_word = enc_word.decode('utf-8')
    print(f'Строковое представление:\n {dec_word}\n {type(dec_word)}')
