#! /usr/bin/python
# -*- coding: utf-8 -*-
from matplotlib import pylab as pl
import os


def main():
    if not os.path.exists('images'):
        os.mkdir('images')
    if not os.path.exists('images/pos'):
        os.mkdir('images/pos')
    if not os.path.exists('images/neg'):
        os.mkdir('images/neg')
    with open('data.txt') as f:
        lines = f.read().split('\n')
        for idx, line in enumerate(lines[:-1]):
            tmp = line.split(' ')
            items = tmp[1].split(';')
            x = list()
            y = list()
            t = list()
            for i in items:
                pos = i.split(',')
                if len(pos) == 3:
                    x.append(pos[0])
                    y.append(pos[1])
                    t.append(pos[2])
            sx = items[0].split(',')[0]  # 轨迹起点x
            sy = items[0].split(',')[1]  # 轨迹终点y
            ex = tmp[2].split(',')[0]  # 目标坐标x
            ey = tmp[2].split(',')[1]  # 目标坐标y
            title = 'People' if tmp[-1] == '1' else 'Machine'
            pl.plot(x, y, 'g-', x, y, 'ro', lw=1, ms=2)
            pl.title(title)
            pl.scatter(sx, sy, color='blue')
            # pl.scatter(ex, ey, color='black')
            if tmp[-1] == '0':
                pl.savefig('images/neg/' + str(idx + 1) + '-' + tmp[-1] + '.png')
            else:
                pl.savefig('images/pos/' + str(idx + 1) + '-' + tmp[-1] + '.png')
            pl.show()
if __name__ == '__main__':
    main()
