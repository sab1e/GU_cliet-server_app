"""
5. Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
преобразовать результаты из байтовового в строковый тип на кириллице.

Подсказки:
--- используйте модуль chardet
"""

import subprocess
import chardet

ACTION = 'ping'
RESOURSCES = ['yandex.ru', 'youtube.com']

for resource in RESOURSCES:
    ARGS = [ACTION, resource]
    RES_PING = subprocess.Popen(ARGS, stdout=subprocess.PIPE)

    for line in RES_PING.stdout:
        result = chardet.detect(line)
        line = line.decode(result['encoding']).encode('utf-8')
        print(line.decode('utf-8'))
