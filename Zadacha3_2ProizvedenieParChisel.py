# Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент,
# второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

numbers=[int(i) for i in input().split()]
i=0
j=int(len(numbers)-1)
newNumbers=[]
while (i<=j):
    newNumbers.append(numbers[i]*numbers[j])
    i+=1
    j-=1
print(" ".join(str(i) for i in newNumbers))

