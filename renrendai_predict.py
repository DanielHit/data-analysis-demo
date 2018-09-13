# coding=utf-8

# 人人贷定投投资分析
# 人人贷采用定投模式. 每个月投入1W. 定期1年. 按照目前的年华 9.8%计算. 10年定投后总的收入
# 年化收益为 9.8%. 那么月收益为 5.85%.
# 第n个月的收益为  1->n (1 + 5.85%) ** (n)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 120, 121, endpoint=True)

y2 = np.power(1.00783, x)

y3 = np.cumsum(y2)

plt.plot(x, y2)
plt.plot(x , y3)

plt.show()
