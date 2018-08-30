# -*- coding: utf-8 -*-
"""
Created on Wed Aug  8 14:39:12 2018

@author: windows7
"""
import random
print("游戏开始啦！")
print ("请猜0-20之间的整数")

x=random.randint(0,20)#(最小值，最大值)
count=0
while 1:  
    count+=1
    number=int(input("请输入数字："))
    if number==x:
        if count==1:
            print("逆天！一次猜中！")
        elif 1<count<=5:
            print(count,"次就猜中了，佩服佩服")
        else:
            print("一共猜了",count,"次哦！")
        break
    elif number>x:
        print("猜大了")      
    elif number<x:
        print("猜小了")
print("游戏结束！")
