# ------------------------------------2-----------------------------
'''
Создать текстовый файл (не программно), сохранить
в нем несколько строк, выполнить подсчет количества строк,
количества слов в каждой строке.
'''

file_2 = open('file_2.txt', 'r')
content = file_2.read()
print(f'Содержимое файла: \n {content}')
file_2 = open('file_2.txt', 'r')
content = file_2.readlines()
print(f'Количество строк в файле - {len(content)}')
file_2 = open('file_2.txt', 'r')
content = file_2.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - строки {len(content[i])}')
file_2 = open('file_2.txt', 'r')
content = file_2.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
file_2.close()
