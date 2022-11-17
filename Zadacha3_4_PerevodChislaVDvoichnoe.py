# Напишите программу, которая будет преобразовывать десятичное число
# в двоичное.
# Пример:
# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10
number=int(input())
binaryNumber=[]
if number == 0:
    binaryNumber.insert(0,0)
else:
    binaryNumber.insert(0,1)
    while number>=2:
        binaryNumber.insert(1,number%2)
        number=number//2
print("".join(str(i) for i in binaryNumber))
