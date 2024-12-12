import io
def custom_write(file_name, strings): #file_name - название файла для записи, strings - список строк для записи
    file = open(file_name, 'a+', encoding = 'utf - 8')
    string_positions = {}
    file.seek(0)

    for i in range(len(strings)):
        string_positions[i + 1, file.tell()] = strings[i]
        file.write(strings[i] + '\n')

    file.close()

    return string_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
]

result = custom_write('test.txt', info)

for elem in result.items():
    print(elem)
