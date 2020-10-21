"""
Каждое из слов «class», «function», «method» записать в байтовом типе без преобразования в последовательность кодов
(не используя методы encode и decode) и определить тип, содержимое и длину соответствующих переменных.
"""

cls = 'class'
fnc = 'function'
mth = 'method'
b_cls = b'class'
b_fnc = b'function'
b_mth = b'method'

my_list = [cls, b_cls, fnc, b_fnc, mth, b_mth]

for i in my_list:
    print(f'{type(i)} --- {i}--- {len(i)}')
