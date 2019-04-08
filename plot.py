# -*- coding: utf-8 -*-
"""
Created on Tue Feb 06 15:22:26 2018

@author: m.nagano
"""
import numpy as np
import matplotlib.pyplot as plt
import os

table2 = np.loadtxt('z.txt').T

path = './graph/'
if not os.path.isdir(path):
    os.mkdir(path)

for i in range(len(table2[0])):
   plt.plot(table2[0],table2[1],label = "Data 1")

   plt.plot(table2[0][i],table2[1][i],'o')
   plt.legend()
   plt.savefig("%s%d.png" %(path,i))
   plt.close()

