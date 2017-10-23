# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 14:56:48 2017

@author: hiroya
"""


class Figure:
    def showPlots(self, plots):
        x = plots[:, 0]
        y = plots[:, 1]
        plt.plot(x, y, 'ro')
        plt.show()
