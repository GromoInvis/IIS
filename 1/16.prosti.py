def is_prime(b):
    if b <= 1:
        return False
    if b <= 3:
        return True
    if b % 2 == 0 or b % 3 == 0:
        return False
    i = 5
    while i * i <= b:
        if b % i == 0 or b % (i + 2) == 0:
            return False
        i += 6
    return True
N = int(input("Введіть значення N: "))
a = [b for b in range(1, N + 1) if is_prime(b)]
print(f"Список простих чисел від 1 до {N}: {a}")
