# Assignment 2: 二维无旋转流体流动场 (源流与涡旋流)
# 学生姓名:
# 学号:
# 教程小组:

import numpy as np
import matplotlib.pyplot as plt

# 计算二维点源（或点汇）速度场
def source_flow(Q, X, Y):
    r = np.sqrt(X**2 + Y**2) + 1e-10  # 防止除零错误
    u = (Q / (2 * np.pi)) * (X / r**2)
    v = (Q / (2 * np.pi)) * (Y / r**2)
    return u, v

# 计算二维涡旋速度场
def vortex_flow(Gamma, X, Y):
    r = np.sqrt(X**2 + Y**2) + 1e-10
    u = - (Gamma / (2 * np.pi)) * (Y / r**2)
    v = (Gamma / (2 * np.pi)) * (X / r**2)
    return u, v

# 定义网格
x = np.linspace(-2, 2, 100)
y = np.linspace(-2, 2, 100)
X, Y = np.meshgrid(x, y)

# 参数设置
Q = 5.0        # 源流强度（Q>0为源，Q<0为汇）
Gamma = 5.0    # 涡旋环流强度

# 计算速度场
u_source, v_source = source_flow(Q, X, Y)
u_vortex, v_vortex = vortex_flow(Gamma, X, Y)

# 绘制点源流场矢量图 (quiver)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.quiver(X, Y, u_source, v_source, color='blue')
plt.title('Point Source Flow (Quiver)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

# 绘制涡旋流场流线图 (streamplot)
plt.subplot(1, 2, 2)
plt.streamplot(X, Y, u_vortex, v_vortex, density=2, linewidth=1, arrowsize=1.5, color='red')
plt.title('Vortex Flow (Streamplot)')
plt.xlabel('x')
plt.ylabel('y')
plt.axis('equal')

plt.tight_layout()
plt.show()