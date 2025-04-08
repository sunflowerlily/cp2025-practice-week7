### 📌 `problem1.py`

# Problem 1: 绘制 cos(tan(pi*x))
# 姓名：
# 学号：
# 小组：

import sympy as sp
from sympy.plotting import plot

x = sp.symbols('x')
expr = sp.cos(sp.tan(sp.pi * x))
plot(expr, (x, -1, 1), xlabel='x', ylabel='f(x)', title='cos(tan(pi*x))')

# Problem 2: 绘制隐函数 e^y + cos(x)/x + y = 0
# 姓名：
# 学号：
# 小组：

import sympy as sp
from sympy.plotting import plot_implicit

x, y = sp.symbols('x y')
expr = sp.exp(y) + sp.cos(x)/x + y
plot_implicit(expr, (x, -10, 10), (y, -10, 10), xlabel='x', ylabel='y',
              title='Implicit plot of exp(y) + cos(x)/x + y = 0', points=500)

# Problem 3: 绘制参数曲面
# 姓名：
# 学号：
# 小组：

import sympy as sp
from sympy.plotting import plot3d_parametric_surface

s, t = sp.symbols('s t')
x = sp.exp(-s)*sp.cos(t)
y = sp.exp(-s)*sp.sin(t)
z = t

plot3d_parametric_surface(x, y, z, (s, 0, 8), (t, 0, 5*sp.pi),
                          xlabel='x', ylabel='y', zlabel='z',
                          title='Parametric Surface Plot')