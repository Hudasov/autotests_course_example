# Дан текстовый файл test_file/task1_data.txt
# Он содержит текст, в словах которого есть цифры.
# Необходимо удалить все цифры и записать получившийся текст в файл test_file/task1_answer.txt


# Здесь пишем код

with open("test_file/task1_data.txt", encoding="utf-8") as file_1:
    file1 = file_1.readlines()
with open("test_file/task1_answer.txt", mode="w+", encoding="utf-8") as file_2:
    for one_line in file1:
        for c in one_line:
            if not c.isdigit():
                file_2.write(c)
    file_2.seek(0)
    file2 = file_2.readlines()

# Ниже НИЧЕГО НЕ НАДО ИЗМЕНЯТЬ


with open("test_file/task1_answer.txt", 'r', encoding='utf-8') as file1:
    with open("test_file/task1_ethalon.txt", 'r', encoding='utf-8') as file2:
        answer = file1.readlines()
        ethalon = file2.readlines()
        assert answer == ethalon, "Файл ответа не совпадает с эталонном"
print('Всё ок')
