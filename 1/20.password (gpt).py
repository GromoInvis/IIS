import random
import string

# Запитуємо користувача про довжину паролю
password_length = int(input("Введіть довжину паролю: "))

# Створюємо список символів, з яких буде генеруватися пароль
characters = string.ascii_letters + string.digits + string.punctuation

# Генеруємо випадковий пароль
password = ''.join(random.choice(characters) for i in range(password_length))

# Виводимо випадковий пароль
print("Ваш випадковий пароль:", password)
