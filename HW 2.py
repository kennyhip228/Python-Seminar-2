# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике.
# Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки.
# Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.
import math

def findNumbers(sumOfNumbers, prodOfNumbers):
    discriminant = sumOfNumbers**2 - 4*prodOfNumbers
    if discriminant < 0:
        print(f'нет решения')
    else:
        x = (sumOfNumbers + math.sqrt(discriminant)) / 2
        y = (sumOfNumbers - math.sqrt(discriminant)) / 2
        if x*y != prodOfNumbers or x+y != sumOfNumbers:
            print("Вы ввели неверные значения")
        else:
            print(f'Вы загадали числа {round(x)} и {round(y)}')

sumOfNumbers = int(input("Введите сумму двух загаданных чисел: "))
prodOfNumbers = int(input("Введите произведение этих же чисел: "))
findNumbers(sumOfNumbers, prodOfNumbers)
