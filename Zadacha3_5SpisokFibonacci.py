# Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: 
# [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
# [Негафибоначчи]

number=int(input())
fibo=[1,0,1]
for i in range(number-1):
    positiveDigit=fibo[-1]+fibo[-2]
    negativeDigit=(-1)**(i+1)*positiveDigit
    fibo.append(positiveDigit)
    fibo.insert(0,negativeDigit)
print(" ".join(str(i) for i in fibo))