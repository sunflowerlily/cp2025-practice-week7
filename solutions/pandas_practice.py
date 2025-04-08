import ssl
ssl._create_default_https_context = ssl._create_unverified_context

import numpy as np, matplotlib.pyplot as plt
import pandas as pd

skiprows = [i for i in range(22) if i not in [0,1,8,11]] #not in []是需要保留的列
# The data is stored in multiple tables on the webpage. Let's fetch all of them.
tables = pd.read_html("https://nssdc.gsfc.nasa.gov/planetary/factsheet",
                      skiprows=skiprows, #去掉不需要的列
                      index_col=0, #设置索引列
                      header=0  #以第一行作为表头
                     )
df = tables[0].T #表格转置，行列互换
df.drop(['MOON'],inplace=True) #去掉关于月亮的行
df = df.astype(float)
