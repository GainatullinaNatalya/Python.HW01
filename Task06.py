# Напишите программу, которая принимает на вход цифру, 
# обозначающую день недели, и проверяет, является ли этот день выходным

print('Введите номер дня недели, чтобы проверить является ли он выходным: ')
day = int(input())

if day == 6 or day == 7:
    print('Да')
elif 0 < day < 6:
    print('Нет')
else:
    print('Нет такого дня недели')