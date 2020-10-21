"""
Выполнить пинг веб-ресурсов yandex.ru, youtube.com
и преобразовать результаты из байтовового в строковый тип на кириллице.
"""

import subprocess
import chardet

args = ['ping', 'yandex.ru']

subproc_ping = subprocess.Popen(args, stdout=subprocess.PIPE)

for line in subproc_ping.stdout:
    result = chardet.detect(line)
    line = line.decode(result['encoding']).encode('UTF-8')
    line = line.decode('UTF-8')
    print(line)
