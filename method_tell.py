def custom_write(file_name, strings):
    file = open(file_name,'w+', encoding= 'utf-8')
    strings_position = {}
    for i in range(len(strings)):
        strings_position[i+1, file.tell()] = strings[i]
        file.write(strings[i])
        file.write('\n')
    file.close()

    return strings_position

info = [
    'Text for tell',
    'Используйте кодировку UTF-8',
    'Because there are 2 languages!',
    'Спасибо!'
]
result = custom_write('test.txt',info)
for elem in result.items():
    print(elem)
