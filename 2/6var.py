import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #розширення функціоналу matplotlib
import numpy as np

# Завантаження даних
data = pd.read_csv("phones_data.csv")

# 1. Побудуйте стовпчикову діаграму розподілу цін на смартфони.

plt.figure(figsize=(15, 5))
plt.bar(data["brand_name"], data["best_price"], label="Ціна, грн", color="red")
plt.xticks (rotation= 90 , fontsize = "6")
plt.legend()
plt.show()

# 2. Визначте, як залежить ціна на смартфон від діагоналі екрану.

plt.figure(figsize=(10, 5))
plt.stem(data["screen_size"], data["best_price"])
plt.xlabel("Діагональ екрану, дюйми")
plt.ylabel("Ціна, грн")
plt.title("Залежність ціни від діагоналі екрану")
plt.show()

# 3. Знайдіть ТОП-5 найдешевших смартфонів з найбільшою ємністю акумулятора.

data = data[data["battery_size"] >= 5000]
data = data.sort_values("best_price", ascending=True).head(5)
print(data)

# 4. Створіть кругову діаграму розподілу долі виробників смартфонів на ринку (візьміть лише перші 10 виробників з найбільшою кількістю смартфонів).

data = pd.read_csv("phones_data.csv")
manufacturers = data["brand_name"].value_counts().head(10)
plt.figure(figsize=(10, 5))
plt.pie(manufacturers, labels=manufacturers.index, autopct="%.2f%%")
plt.show()

# 5. Який смартфон виробника Samsung є найбільш популярним в ціновій категорії 10-15 тис. грн?

samsung_phones = data[data["popularity"] == "Samsung"]
samsung_phones = samsung_phones[samsung_phones["best_price"] >= 10000]
samsung_phones = samsung_phones[samsung_phones["best_price"] <= 15000]
print(samsung_phones["model_name"].value_counts().head(1))
