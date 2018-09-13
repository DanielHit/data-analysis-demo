# coding=utf-8

# 人人贷定投投资分析
# 人人贷采用定投模式. 每个月投入1W. 定期1年. 按照目前的年华 9.8%计算. 10年定投后总的收入
# 年化收益为 9.8%. 那么月收益为 0.783%.
# 第n个月的收益为  1->n (1 + 0.783%) ** (n)

import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(1, 240, 240, endpoint=True)

y2 = np.power(1.00783, x)
y21 = np.power(1.00783, x) * 2

y3 = np.cumsum(y2)
y4 = np.cumsum(y21)


plt.plot(x, y3, label='invest 1w per month')
plt.plot(x, y4,label='invest 2w per month')

plt.legend(loc='upper left', frameon=False)

plt.show()
