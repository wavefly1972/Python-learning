# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 18:34:04 2017

@author: 100419
"""

from sklearn.datasets import load_digits

digits=load_digits()
print(digits.data.shape)

import pylab as pl
pl.gray()
pl.matshow(digits.images[1700])
pl.show()

#(1797,64)：表示有1797張圖片(行)，每張圖片是8*8=64相素，所有相素都是一個特徵值