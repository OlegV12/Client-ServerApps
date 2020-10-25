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

import chardet
import re
import csv

my_lst = ['info_1.txt', 'info_2.txt', 'info_3.txt']


def get_data(files_list):
    main_data = ['Изготовитель системы', 'Название ОС', 'Код продукта', 'Тип системы', ]
    os_prod_list = []
    os_name_list = []
    os_code_list = []
    os_type_list = []
    pattern = r'\d{5}[-]\w{3}[-]\d{7}[-]\d{5}'

    pattern_1 = r'(?<=Изготовитель системы:).*(?=\r)'
    pattern_2 = r'(?<=Название ОС:).*(?=\r)'
    pattern_3 = r'(?<=Тип системы:).*(?=\r)'

    for file in files_list:
        with open(file, mode='rb') as f:
            data = f.read()

            coding = chardet.detect(data)
            data = data.decode(encoding=coding['encoding'])

            prod = re.search(pattern_1, data)
            os_prod_list.append(prod.group(0).strip(' '))

            name = re.search(pattern_2, data)
            os_name_list.append(name.group(0).strip(' '))

            os_type = re.search(pattern_3, data)
            os_type_list.append(os_type.group(0).strip(' '))

            res = re.search(pattern, data)
            os_code_list.append(res.group(0))
    return main_data, os_prod_list, os_name_list, os_code_list, os_type_list


def write_to_csv():
    result = get_data(my_lst)
    main_data_list, os_prod_list, os_name_list, os_code_list, os_type_list = result
    data = list(zip(os_prod_list, os_name_list, os_code_list, os_type_list))
    with open('test.csv', 'w') as f_n:
        f_n_writer = csv.writer(f_n)
        f_n_writer.writerow(main_data_list)
        for row in data:
            f_n_writer.writerow(row)


write_to_csv()
