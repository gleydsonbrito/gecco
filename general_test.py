from src.storage import get_csv
import matplotlib.pyplot as plt
import numpy as np

items = get_csv()

s_items = sorted(items, key=lambda i: i[0], reverse=True)
x: float = []
y: float = []

for i in s_items:
    if i[0] < 1000:
        x.append(i[1][7])
        y.append(i[0])

plt.scatter(y, x)
plt.ylabel("Fitness")
plt.xlabel("Values")

z = np.polyfit(y, x, 1)
p = np.poly1d(z)
plt.plot(y, p(y), "r--")

plt.show()
