print("Виберіть операцію конвертації:")
print("1. Цельсій в Фаренгейт")
print("2. Фаренгейт в Цельсій")
a = input("Ваш вибір (1 або 2): ")
if a == '1':
    c = float(input("Введіть температуру в градусах Цельсія: "))
    f = (c * 9/5) + 32
    print(f"Температура в градусах Фаренгейта: {f}°F")
elif a == '2':
    f = float(input("Введіть температуру в градусах Фаренгейта: "))
    c = (f - 32) * 5/9
    print(f"Температура в градусах Цельсія: {c}°C")
else:
    print("Неправильний вибір. Будь ласка, виберіть 1 або 2.")
