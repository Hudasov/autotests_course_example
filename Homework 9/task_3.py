# Дан файл test_file/task_3.txt можно считать, что это запись покупок в магазине, где указана только цена товара
# В каждой строке файла записана цена товара.
# Покупки (т.е. несколько подряд идущих цен) разделены пустой строкой
# Нужно найти сумму трёх самых дорогих покупок, которые запишутся в переменную three_most_expensive_purchases

# Здесь пишем код
with open("test_file/task_3.txt", encoding="utf-8") as purchases:
    purch = purchases.readlines()
my_dict = {}
a = 1
for i in purch:
    if i == "\n":
        a += 1
    else:
        my_dict.setdefault(a, []).append(int(i.strip()))

sorted_result_purchases = sorted(map(lambda x: sum(x), my_dict.values()))
three_most_expensive_purchases = sorted_result_purchases[-1] + sorted_result_purchases[-2] + sorted_result_purchases[-3]
assert three_most_expensive_purchases == 202346
