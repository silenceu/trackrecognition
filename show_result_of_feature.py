#! /usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pylab as pl
from matplotlib import pyplot as pyl


with open('feature.txt') as f:
    y=f.read().split('\n')
    y=y[:-1]
    x=[n for n in range(1,3001)]
    # pl.plot(x, y, 'g-', x, y, 'o', lw=1, ms=2)

    pl.plot(x, y, x, y, 'o', lw=1, ms=2)

    pl.show()
    pyl.clf()

    # pl.scatter(sx, sy, color='blue')
    # pl.scatter(ex, ey, color='blue')
    # pl.scatter(goal_x, goal_y, color='black')

