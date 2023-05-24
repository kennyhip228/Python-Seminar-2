# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

number = int(input("Введите число: "))
powerOfTwo = 1

while powerOfTwo < number:
    powerOfTwo *= 2
    if powerOfTwo < number:
        print(powerOfTwo, end=" ")