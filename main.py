# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 14:02:37 2017

@author: hiroya
"""

# %% import部
import numpy as np
import matplotlib.pyplot as plt
from Proccess import *
from Element import Element

# %%表面力を読み込む

#f = readF()

# %% 座標と接点番号をファイルから読み込む

plots = readPlots()
print(plots[0])

# %% 座標から要素分割を行う

elements = makeElements(plots)
for i in elements:
    print(i.getK())

# %% デバッグ用
