# Assignment 3: 载流直导线磁场矢量场模拟
# 学生姓名:
# 学号:
# 教程小组:

import numpy as np
import matplotlib.pyplot as plt
from scipy.constants import mu_0

# 计算二维空间载流直导线磁场矢量场
def wire_magnetic_field(I, X, Y, wire_pos=(0,0)):
    x0, y0 = wire_pos
    X_shifted = X - x0
    Y_shifted = Y - y0
    r = np.sqrt(X_shifted**2 + Y_shifted**2) + 1e-10  # 避免除零
    B_magnitude = mu_0 * I / (2 * np.pi * r)
    # 磁场方向：垂直于径向，使用圆周方向
    Bx = -B_magnitude * Y_shifted / r
    By = B_magnitude * X_shifted / r
    return Bx, By

# 定义二维计算网格
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# 参数设置
I = 10  # 电流强度（单位：安培）

# 计算磁场
Bx, By = wire_magnetic_field(I, X, Y)

# 绘制磁场矢量图 (quiver)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.quiver(X, Y, Bx, By, color='green', pivot='mid', scale=50)
plt.title('Magnetic Field around Wire (Quiver)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

# 绘制磁场流线图 (streamplot)
plt.subplot(1, 2, 2)
plt.streamplot(X, Y, Bx, By, color='purple', density=2, linewidth=1, arrowsize=1.5)
plt.title('Magnetic Field around Wire (Streamplot)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

plt.tight_layout()
plt.show()