#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 19:02:41 2020

@author: ivy_kosater


Fizz Buzz!

"""

def FizzBuzz(x,y,n):
    for i in range(1,n+1):
        if i % (x*y) == 0:
            print("FizzBuzz")
        elif i % x == 0:
            print("Fizz")
        elif i % y == 0:
            print("Buzz")
        else:
            print(i)
FizzBuzz(3,5,1000)
            