a = input("Введіть список чисел через пробіл: ")
a = a.split()
a = [float(x) for x in a]
b = 0
c = 0
for num in a:
    b += num
    c += 1
if c > 0:
    ser = b / c
    print(f"Середнє значення списку: {ser}")
else:
    print("Список порожній, неможливо знайти середнє значення.")
