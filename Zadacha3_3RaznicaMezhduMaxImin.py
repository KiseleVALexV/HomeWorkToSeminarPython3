# Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу
# между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math
numbers=[i for i in map(float, input().split())]
maxi=numbers[0]-int(numbers[0])
mini=numbers[0]-int(numbers[0])
for i in range(1, len(numbers)): 
    if numbers[i]-int(numbers[i])>maxi:
        maxi=numbers[i]-round(numbers[i])
    if numbers[i]-int(numbers[i])<maxi and numbers[i]-int(numbers[i])!=0:
        mini=numbers[i]-round(numbers[i])
print(round(maxi-mini,2))
