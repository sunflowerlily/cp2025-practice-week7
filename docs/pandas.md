# pandas获取行星数据

本项目通过pandas获取 NASA 提供的太阳系行星数据，利用开普勒第三定律计算行星轨道周期，并绘制轨道周期与半长轴的关系图像，导出数据到Excel文件。

## 📚 物理背景

开普勒第三定律描述了行星轨道周期（T）与轨道半长轴（a）的关系：

$$
T^2 \propto a^3
$$

对于以太阳为中心的行星轨道，开普勒第三定律可表达为：

$$
T = \sqrt{\frac{4\pi^2}{GM}}a^{3/2}
$$

其中：

-  $T$：轨道周期（秒）
-  $a$：轨道半长轴（米）
-  $G$：引力常数（ $6.67430 \times 10^{-11}\,\text{m}^3\,\text{kg}^{-1}\,\text{s}^{-2}$）
-  $M$：太阳质量（约为 $1.989\times10^{30}$ kg）

## 🎯 项目任务

- 使用pandas抓取[Planetary Fact Sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/)的数据表；
- 利用pandas的工具提取行星质量、轨道半长轴数据；
- 利用开普勒第三定律计算轨道周期；
- 绘制轨道周期与半长轴的关系；
- 将计算结果导出为Excel文件。

## 🚀 快速开始

安装依赖：

```bash
pip install -r requirements.txt