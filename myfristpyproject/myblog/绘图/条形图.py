import numpy as np
import matplotlib.pyplot as plt

for i in range(0, 15):
    # 1 柱状图
    dateOne = np.zeros([2])
    dateOne[0] = i;
    dateOne[1] = i;
    y = np.zeros([2])
    y[0] = 10
    y[1] = 20
    plt.plot(dateOne, y, 'r', lw=8)
plt.show()
