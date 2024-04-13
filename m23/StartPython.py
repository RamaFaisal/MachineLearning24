print("Hello World!")
height = 2.0
print(type(height))
tall = True
# height1 = 1.84
# height2 = 1.79
# height3 = 1.82
# height4 = 1.90
# type(height)
# int
height = [1.84, 1.79, 1.82, 1.90, 1.80]
print(height)
height = [2, 1.79, 1.82, 1.90, 1.80]
print(height, type(height))
famz = ["Abe", 1.84, "Beb", 1.79, "Cory", 1.82, "Dad", 1.90]
print(famz)
weight = [66.5, 60.3, 64.7, 89.5, 69.8]
print(weight)

import numpy as np
np_height = np.array(height)
print(type(np_height))
np_weight = np.array(weight)
print(np_weight)
bmi = np_weight / np_height ** 2
print(type(np_weight))
print(bmi)
print(np)
np_2d = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_2d)
print(np_2d.shape)
import pandas as pd
Tab = pd.read_csv("Tab.csv")
print(Tab)
print(Tab["Negara"], type)
print(Tab.Ibukota, type)

import matplotlib.pyplot as plt
year = [1980, 1990, 2000, 2010, 2020]
price = [2.5, 7.6, 9.7, 15.8, 22.9]
plt.scatter(year, price)
plt.plot(year, price)
plt.show()