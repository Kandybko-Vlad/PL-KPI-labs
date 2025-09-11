# Розгорнути задане тризначне число задом наперед.
a = int(input("Введіть тризначне число, яке хочете обернути: "))
b = a % 10 # the last number
c = a // 100 # the first number
d = (a // 10) % 10 # the middle number
x = b * 100 + d * 10 + c
print("Обернуте число:", x)
