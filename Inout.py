# -*- coding: utf-8 -*-
"""
Created on Fri Oct 13 17:00:42 2017

@author: hiroya
"""

import numpy as np
import matplotlib.pyplot as plt


def hello():
    print("hello")

def readFile(filename):
    plots = np.loadtxt(filename, delimiter=',', skiprows=1, dtype=float)
    return plots

def showPlots(plots):
    x = plots[:, 0]
    y = plots[:, 1]
    plt.plot(x, y, 'ro')
    for i in range(x.size):
        plt.text(x[i], y[i], i, ha='center', va='top')
    plt.show()

def showMakingElements(plots, elementIndexList):
    x = plots[:, 0]
    y = plots[:, 1]
    plt.plot(x, y, 'ro')
    for i in range(x.size):
        plt.text(x[i], y[i], i, ha='center', va='top')
    for elementIndex in elementIndexList:
        line_x = []
        line_y = []
        for i in range(len(elementIndex)):
            line_x.append(x[elementIndex[i]])
            line_y.append(y[elementIndex[i]])
        line_x.append(x[elementIndex[0]])
        line_y.append(y[elementIndex[0]])
        plt.plot(line_x, line_y, 'r-')
    plt.show()
