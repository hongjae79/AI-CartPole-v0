#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 11 21:33:17 2018

@author: jason
"""

from __future__ import print_function, division

import numpy as np
import RBF

class SGDRegressor:
    print('Numpy Rules')
    def __init__(self, D):
        self.w = np.random.randn(D) / np.sqrt(D)
        self.lr = 0.1

    def partial_fit(self, X, Y):
        self.w += self.lr*(Y - X.dot(self.w)).dot(X)

    def predict(self, X):
        return X.dot(self.w)
    
if __name__ == '__main__':
  RBF.SGDRegressor = SGDRegressor
  RBF.main()