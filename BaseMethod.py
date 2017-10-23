# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 17:48:17 2017

@author: hiroya
"""


def elementIndexListToPlots(plots, elementIndexList):
    elementPlots = []
    for elementIndex in elementIndexList:
        tmpPlot = []
        for i in range(len(elementIndex)):
            tmp = plots[elementIndex[i], :]
            tmpPlot.append(tmp)
        elementPlots.append(tmpPlot)
    return elementPlots
