# -*- coding: utf-8 -*-
"""
Created on Thu Aug 16 14:28:02 2018

@author: windows7
"""

age=int(input("狗狗年龄："))
if age<0:
    print("你在逗我吧")
elif age==1:
    print("主子14岁了呢！")
elif age==2:
    print("主子24岁了哦")
elif age>2:
    human=22+(age-2)*5
    print("主子现在的年龄是：",human)
input("点击Enter结束")