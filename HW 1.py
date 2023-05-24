# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

amountOfCoins = int(input("Введите количество монет: "))
coins = []
tail = 0
eagle = 0
minCoins = 0

for i in range(amountOfCoins):
    temp = random.randint(0, 1)
    coins.append(temp)
print(f'Положение монет: {coins}')

for i in coins:
    if i == 0:
        eagle += 1
    else:
        tail += 1

if eagle <= tail:
    minCoins = eagle
else:
    minCoins = tail

print(f'Минимальное количество монет, которые нужно перевернуть: {minCoins}')