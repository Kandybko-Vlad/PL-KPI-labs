#Перевірити, чи є в масиві число 7.
l = []
c = 7
a = int(input("Скільки елементів Ви бажаєте мати в списку?\n"))
for i in range(a):
    b = int(input(f"Введіть елемент №{i+1}:"))
    l.append(b)
if c in l:
    print("Сімку знайдено")
else:
    print("Сімки нема")