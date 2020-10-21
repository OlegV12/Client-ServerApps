"""Определить, какие из слов «attribute», «класс», «функция», «type»
невозможно записать в байтовом типе."""

attr = 'attribute'
cls = 'класс'
fnc = 'функция'
typ = 'type'

my_list = [attr, cls, fnc, typ]

for i in my_list:
    try:
        print(bytes(i, encoding='ASCII'))

    except UnicodeEncodeError:
        print(f'из за кодировки невозможен перевод в байты "{i}"')
        res = bytes(i, encoding='UTF-8')
        print(bytes(res))
