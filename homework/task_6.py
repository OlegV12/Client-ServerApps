"""
Создать текстовый файл test_file.txt, заполнить его тремя строками:
«сетевое программирование», «сокет», «декоратор».
Проверить кодировку файла по умолчанию.
Принудительно открыть файл в формате Unicode и вывести его содержимое.
"""

import locale

default_coding = locale.getpreferredencoding()

with open('test_file.txt', encoding=default_coding) as f:
    for line in f:
        print(line)

print(default_coding)
