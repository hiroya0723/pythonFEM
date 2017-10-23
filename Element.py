# -*- coding: utf-8 -*-
"""
Created on Mon Oct 16 21:22:06 2017

@author: hiroya
"""
import numpy as np


class Element(object):
    h = 1
    nu = 1/3.0
    E = 100

    def __init__(self, elementPlot, elementIndex):
        self.plots = elementPlot
        self.index = elementIndex

        self.l = self.makeL(self.plots)
        self.A = self.makeA(self.plots)
        self.B = self.makeB(self.plots)
        self.D = self.makeD()
        self.K = self.makeK(self.A, self.B, self.D)

    def getPlots(self):
        return self.plots

    def getIndex(self):
        return self.index

    def getA(self):
        return self.A

    def getB(self):
        return self.B

    def getD(self):
        return self.D

    def getK(self):
        return self.K

    def makeL(self, plots):
        l = []
        size = len(plots)
        for i in range(size):
            p = plots[i % size] - plots[(i+1) % size]
            ltmp = np.linalg.norm(p)
            l.append(ltmp)
        return l

    def makeA(self, plots):
        u = plots[2] - plots[0]
        v = plots[1] - plots[0]
        a = np.cross(u, v)
        A = np.linalg.norm(a)/2.0
        return A

    def makeB(self, plots):
        x1 = plots[0][0]
        x2 = plots[1][0]
        x3 = plots[2][0]
        y1 = plots[0][1]
        y2 = plots[1][1]
        y3 = plots[2][1]
        b = [[y2-y3, 0,     y3-y1, 0,     y1-y2, 0],
             [0,     x3-x2, 0,     x1-x3, 0,     x2-x1],
             [x3-x2, y2-y3, x1-x3, y3-y1, x2-x1, y1-y2]
            ]
        B = np.array(b)/(2*self.A)
        return B

    def makeD(self):
        nu = self.nu

        d = [[1, nu, 0],
             [nu, 1, 0],
             [0, 0, (1-nu)/2]
            ]
        D = np.array(d)*self.E/(1-nu**2)
        return D

    def makeK(self, A, B, D):
        #K = A*self.h*B.T*D*B
        K = np.dot(B.T, D)
        K = np.dot(K, B)
        K = K*A*self.h
        return K

    def test(self):
        return self.h*2
