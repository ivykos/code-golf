#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 16:17:20 2020

@author: ivy_kosater

Fibb Sequence

Fn = Fn-1 + Fn-2

Example 1, 1, 2, 3, 5, 8, 13, 21, etc. etc....

Write function that takes integer n, and returns
the nth Fibb number
"""

def fibs(n):
    if n < 0:
        print("Invalid")
    elif n == 1:
        return 0
    elif n ==2:
        return 1
    else:
        return fibs(n-1) + fibs(n-2)

