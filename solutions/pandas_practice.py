import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# 常数定义
G = 6.67430e-11          # 引力常数（m^3/kg/s^2）
M_sun = 1.989e30         # 太阳质量（kg）

# TODO 1: 使用pandas读取网页数据
def fetch_planet_data(url):
    tables = pd.read_html(url)
    df = tables[0]
    return df

# TODO 2: 提取轨道半长轴（Distance from Sun）并转换为米
def extract_semi_major_axis(df):
    semi_major_axis_km = df.loc[:, 'Distance from Sun (106 km)'] * 1e6  # km
    semi_major_axis_m = semi_major_axis_km * 1e3  # 转换为米
    return semi_major_axis_m

# TODO 3: 用开普勒第三定律计算周期并转换为年
def calculate_orbital_period(a):
    T_seconds = np.sqrt((4 * np.pi ** 2 / (G * M_sun)) * a ** 3)
    T_years = T_seconds / (60 * 60 * 24 * 365.25)  # 转换为年
    return T_years

# TODO 4: 绘制周期与半长轴关系
def plot_period_vs_axis(a, T):
    plt.figure(figsize=(8, 5))
    plt.plot(a / 1.496e11, T, 'o-', color='blue')
    plt.xlabel('Semi-major Axis (AU)')
    plt.ylabel('Orbital Period (years)')
    plt.title('Kepler\'s Third Law: Orbital Period vs Semi-major Axis')
    plt.grid(True)
    plt.show()

# TODO 5: 将数据保存到Excel文件
def save_to_excel(a, T, filename='planet_periods.xlsx'):
    df = pd.DataFrame({
        'Semi-major Axis (AU)': a / 1.496e11,
        'Orbital Period (years)': T
    })
    df.to_excel(filename, index=False)

def main():
    url = 'https://nssdc.gsfc.nasa.gov/planetary/factsheet/'
    df = fetch_planet_data(url)

    a = extract_semi_major_axis(df)
    T = calculate_orbital_period(a)

    plot_period_vs_axis(a, T)
    save_to_excel(a, T)

if __name__ == "__main__":
    main()