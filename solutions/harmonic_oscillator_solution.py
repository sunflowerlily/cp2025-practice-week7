import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# 简谐振子参数
m = 1.0       # 质量
k = 1.0       # 弹簧常数
x0 = 1.0      # 初始位置
v0 = 0.0      # 初始速度

# 时间区间
t = np.linspace(0, 10, 200)

# TODO 1: 使用SymPy符号求解简谐振子微分方程
def symbolic_solution(m, k, x0, v0):
    t_sym = sp.symbols('t', real=True)
    x = sp.Function('x')(t_sym)
    
    # 定义运动微分方程
    eq = sp.Eq(m * x.diff(t_sym, 2) + k * x, 0)

    # 求解方程，应用初始条件
    sol = sp.dsolve(eq, ics={x.subs(t_sym, 0): x0, x.diff(t_sym).subs(t_sym, 0): v0})

    return sol

# TODO 2: 使用odeint数值求解简谐振子微分方程
def numeric_solution(m, k, x0, v0, t):
    def oscillator_eq(y, t, m, k):
        x, v = y
        dydt = [v, -k/m * x]
        return dydt

    y0 = [x0, v0]
    sol_numeric = odeint(oscillator_eq, y0, t, args=(m, k))
    return sol_numeric[:, 0]

# TODO 3: 绘制符号解与数值解对比图
def plot_solutions():
    symbolic_sol = symbolic_solution(m, k, x0, v0)
    numeric_sol = numeric_solution(m, k, x0, v0, t)

    # 将符号解转为数值函数
    t_sym = sp.symbols('t')
    symbolic_func = sp.lambdify(t_sym, symbolic_sol.rhs, 'numpy')
    symbolic_vals = symbolic_func(t)

    # 创建包含两个子图的图形
    plt.figure(figsize=(12, 6))
    
    # 第一个子图：原始解
    plt.subplot(2, 1, 1)
    plt.plot(t, symbolic_vals, 'r-', label='SymPy symbolic solution')
    plt.plot(t, numeric_sol, 'b--', label='SciPy numeric solution (odeint)')
    plt.xlabel('Time (s)')
    plt.ylabel('Displacement (m)')
    plt.title('Solutions Comparison')
    plt.legend()
    plt.grid(True)
    
    # 第二个子图：差值
    plt.subplot(2, 1, 2)
    difference = symbolic_vals - numeric_sol
    plt.plot(t, difference, 'g+', label='Difference')
    plt.xlabel('Time (s)')
    plt.ylabel('Difference (m)')
    plt.title('Symbolic vs Numeric Difference')
    plt.legend()
    plt.grid(True)
    
    plt.tight_layout()
    plt.show()

# 运行绘图函数
if __name__ == "__main__":
    plot_solutions()