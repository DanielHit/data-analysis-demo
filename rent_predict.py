# coding=utf-8
# 租金与月供的变动曲线

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(2018, 2028, 10, endpoint=True)
y1 = np.power(1.11, x - 2018) * 8000
y2 = np.power(1.09, x - 2018) * 8000
y3 = 13500 * (x - x + 1)

plt.xticks(np.linspace(2018, 2028, 11, endpoint=True))
plt.yticks(np.linspace(7500, 25000, 11, endpoint=True))


plt.plot(x, y1, linestyle="-", label="11% rate")
plt.plot(x, y2, label="9% rate")
plt.plot(x, y3, linestyle="--", label="loans per month")
t = 2023
plt.plot([t,t],[7500,13500], linestyle="--", color ='gray')

# 标记平衡点 | 租金和时间点

plt.annotate('loans == rent',
             xy=(2023, 13500),
             xycoords='data',
             xytext=(+10, +30),
             textcoords='offset points',
             arrowprops=dict(facecolor='red', shrink=0.05),
            )



plt.legend(loc='upper left', frameon=False)


plt.show()


