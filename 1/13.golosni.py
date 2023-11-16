w = input("Введіть слово: ").lower()
a = 0
v = "aeiou"
for letter in w:
    if letter in v:
        a += 1
print(f"Кількість голосних літер у слові '{w}' дорівнює {a}.")
