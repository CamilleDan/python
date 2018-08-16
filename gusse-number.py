# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:39:12 2018

@author: windows7
"""

number=7
guess=-1
while guess!=number:
    guess=int(input("请输入猜测数字："))
    if guess==number:
        print("这么厉害的么？")
    elif guess>number:
        print("猜大了")      
    elif guess<number:
        print("猜小了")
        