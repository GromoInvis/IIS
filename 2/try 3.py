import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #розширення функціоналу matplotlib
import numpy as np

# Завантаження даних
data = pd.read_csv("phones_data.csv")

# Функції для створення діаграм
#Розподіл цін
def plot_bar2_chart():
    plt.figure(figsize=(15, 5))
    plt.bar(data["brand_name"], data["best_price"], label="Ціна, грн", color="red")
    plt.xticks (rotation= 90 , fontsize = "6")
    plt.legend()
    plt.show()
# Розподіл цін
def plot_bar_chart():

    plt.figure(figsize=(10, 5))
    plt.bar(data["best_price"], data["popularity"], label="Ціна, грн")
    plt.xlabel("Ціна, грн")
    plt.ylabel("Кількість смартфонів")
    plt.legend()
    plt.show()
#Залежність ціни від діагоналі екрану
def plot_scatter_chart():
    plt.figure(figsize=(10, 5))
    plt.stem(data["screen_size"], data["best_price"])
    plt.xlabel("Діагональ екрану, дюйми")
    plt.ylabel("Ціна, грн")
    plt.title("Залежність ціни від діагоналі екрану")
    plt.show()
#Кількість смартфонів за виробниками
def plot_pie_chart():
    manufacturers = data["brand_name"].value_counts().head(10)
    plt.figure(figsize=(10, 5))
    plt.pie(manufacturers, labels=manufacturers.index, autopct="%.2f%%")
    plt.show()
#Динаміка ціни в залежності від діагоналі екрану
def plot_line_chart():
    plt.figure(figsize=(12, 8))
    plt.bar(data["screen_size"], data["best_price"], label="Ціна в залежності від діагоналі екрану")
    plt.xlabel("Діагональ екрану, дюйми")
    plt.ylabel("Ціна, грн")
    plt.legend(loc="best", prop={"size": 10})
    plt.show()
#Samsung popularity
def samsung_phone_popular():
    samsung_phones = data[data["popularity"] == "Samsung"]
    samsung_phones = samsung_phones[samsung_phones["best_price"] >= 10000]
    samsung_phones = samsung_phones[samsung_phones["best_price"] <= 15000]
    return samsung_phones["model_name"].value_counts().head(1)

def create_button(name, function):
    button = tk.Button(root, text=name, command=function)
    button.pack()
def insert_data():
    text.insert("end", "", samsung_phone_popular)
# Головне вікно
root = tk.Tk()
root.title("Аналіз даних смартфонів")
root.geometry("800x600")

# Кнопки
create_button("Розподіл цін", plot_bar2_chart)
create_button("Залежність ціни від діагоналі екрану", plot_scatter_chart)
create_button("Кількість смартфонів за виробниками", plot_pie_chart)
create_button("Динаміка ціни в залежності від діагоналі екрану", plot_line_chart)
#text try
text = tk.Text(root, width=200, height=100)
text.insert("end", "", samsung_phone_popular)
text.config(bg="white", fg="black")
# Додаємо виджет Text до вікна програми
text.pack()
# Запускаємо цикл обробки подій


# Запуск вікна
root.mainloop()
