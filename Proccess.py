# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 15:34:14 2017

@author: hiroya
"""

import Inout as io
from BaseMethod import *
from Element import Element
import numpy as np

def hello1():
    print('hello1')


def readPlots():
    plots = io.readFile('plots.csv')
    io.showPlots(plots)
    return plots

def readF():
    f = io.readFile('force.csv')
    print(f)
    return f

def makeElements(plots):
    elementIndexList = []
    elements = []
    for i in range(2):
        print('要素を作るために3点指定して下さい:')
        tmp = input()
        tmp = list(map(int, tmp.split()))
        elementIndexList.append(tmp)
        io.showMakingElements(plots, elementIndexList)
    elementPlotList = elementIndexListToPlots(plots, elementIndexList)
    for (elementPlot, elementIndexList) \
      in zip(elementPlotList, elementIndexList):
        element = Element(elementPlot, elementIndexList)
        elements.append(element)
    return elements

