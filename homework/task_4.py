"""
Преобразовать слова «разработка», «администрирование», «protocol», «standard» из строкового представления в байтовое
и выполнить обратное преобразование (используя методы encode и decode).
"""

dev = 'разработка'
adm = 'администрирование'
protocol = 'protocol'
stnd = 'standard'

my_list = [dev, adm, protocol, stnd]
byte_list = []
res_list = []
for i in my_list:
    byte_list.append(i.encode())

for i in byte_list:
    res_list.append(i.decode())

print(my_list)
print(byte_list)
print(res_list)
