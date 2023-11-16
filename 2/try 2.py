import tkinter as tk
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns #розширення функціоналу matplotlib
import numpy as np

# Завантаження даних
data = pd.read_csv("phones_data.csv")
data.sort_values("popularity", ascending=False)
samsung_phones = data[data["brand_name"] == "Samsung"]
samsung_phones = samsung_phones[samsung_phones["best_price"] >= 10000]
samsung_phones = samsung_phones[samsung_phones["best_price"] <= 15000]

pop = list(samsung_phones["popularity"])
model = list(samsung_phones["model_name"])
dota2 = {}
for i in range(len(pop)):
    dota2[model[i]] = pop[i]
print(dota2)
myList1 = dota2.keys()
myList2 = dota2.values()
sortedData = sorted(myList1, key = lambda x: dota2[x])
print (sortedData)

sortedPop = []
for i in sortedData:
    sortedPop.append(dota2[i])

print(pd.Series(sortedPop, sortedData))