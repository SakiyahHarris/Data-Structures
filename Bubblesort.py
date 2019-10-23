# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 11:24:47 2019

@author: seharris.2018
"""

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i]>alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

alist = [12, 200, 45, 1, 57, 23]
bubbleSort(alist)
print(alist)
