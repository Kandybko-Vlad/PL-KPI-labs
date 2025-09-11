a = int(input("Скільки буде чисел в списку? "))
l = []
for i in range(a):
    b = float(input(f"Введіть число номер {i}"))
    if b % 5 == 0:
        l.append(b)
print(l)
