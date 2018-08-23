# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:39:12 2018

@author: windows7
"""
import random
print ("猜0-20之间的整数")

x=random.randint(0,20)#(最小值，最大值)
count=0
while 1:  
    count+=1
    number=int(input("请输入数字："))
    if number==x:
        print("猜对啦！一共猜了",count,"次哦")
        print("游戏结束！")
        break
    elif number>x:
        print("猜大了")      
    elif number<x:
        print("猜小了")
