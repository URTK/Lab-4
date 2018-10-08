FullName = str(input('Введите ФИО '))

    # Основное задание

print('К-во символов в троке : ', len(FullName))

StringA = FullName.count('А')
Stringa = FullName.count('а')
print ('К-во "A" в ФИО', StringA + Stringa)

    # Разделение ФИО на Ф И О

Nazar = (FullName.split())

    # Задание по варианту

print('В фамилии ', Nazar[1],' содержится', Nazar[1].count('а'),' букв "А"')
