# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random

# Здесь пишем код
import string


def generate_random_name():
    names = []
    for i in range(2):
        s = ""
        for j in range(random.randrange(1, 16)):
            s += random.choice(string.ascii_letters)
        names.append(s)
    yield f"{names[0]} {names[1]}"

print(next(generate_random_name()))
print(next(generate_random_name()))
print(next(generate_random_name()))
print(next(generate_random_name()))

