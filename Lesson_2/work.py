
# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

import random
from random import randint


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = float(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Это не число!")
    return number


def sumNums(num):
    sum = 0
    for i in str(num):
        if i != ".":
            sum += int(i)
    return sum


num = InputNumbers("Введите число: ")

print(f"Сумма цифр = {sumNums(num)}")

# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.


def InputNumbers(inputText):
    is_OK = False
    while not is_OK:
        try:
            number = int(input(f"{inputText}"))
            is_OK = True
        except ValueError:
            print("Число должно быть integer ")
    return number


def mult(n):
    if n == 1:
        return 1
    else:
        return n * mult(n - 1)


num = InputNumbers("Введите число: ")

list = []
for e in range(1, num + 1):
    list.append(mult(e))

print(f"Произведения чисел от 1 до {num}:  {list}")


# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n = int(input('Введите номер: '))


def sequence(n):

    return [round((1 + 1 / x)**x, 2) for x in range(1, n + 1)]


print(sequence(n))
print(round(sum(sequence(n))))

# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

n = int(input('Введите число '))
list = []

for i in range(-n, n+1):
    list.append(i)
print(list)

res = 1
with open('file.txt', 'w') as data:
    data.write('2 \n')
    data.write('1 \n')
    data.write('3 \n')
    data.write('0 \n')
    data.write('5 \n')
    # data.write('4 \n')

patch = 'file.txt'
data = open(patch, 'r')

for line in data:
    pos = int(line)
    res *= list[pos]
print(res)

# Реализуйте алгоритм перемешивания списка.


def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]


def shuffle_list(lst):
    return random.shuffle(lst)


n = 10
lft = -20
rght = 50

mylist = get_list(n, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)
