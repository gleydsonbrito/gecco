from src.storage import get_csv
import matplotlib.pyplot as plt
import numpy as np

items = get_csv()

s_items = sorted(items, key=lambda i: i[0])
x: float = []
y: float = []

for i in s_items:
    if True:
        x.append(i[1][6])
        y.append(i[0])

plt.scatter(x, y)
plt.ylabel("Fitness")
plt.xlabel("Values")

z = np.polyfit(x, y, 1)
p = np.poly1d(z)
plt.plot(x, p(x), "r--")

plt.show()
