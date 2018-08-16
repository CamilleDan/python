# -*- coding: utf-8 -*-
"""
Created on Thu Aug  2 17:39:24 2018

@author: windows7
"""

#画乌龟
import turtle
def draw_diamond(turtle):
    for i in range(1,3):
         #画菱形
        turtle.forward(100)#向前100像素
        turtle.right(45)#向右转45度
        turtle.forward(100)
        turtle.right(135)
    
def draw_art():
    window=turtle.Screen()#获得一个窗口句柄
    window.bgcolor("black")#背景颜色
    #画图区
    brad=turtle.Turtle()#创建turtle实例
    brad.shape("turtle")#形状可以换成圆圈等
    brad.color("red")#颜色红色
    brad.speed("fast")#画图速度快
    #让菱形旋转360度
    for i in range(1,37):
        draw_diamond(brad)#调用diamond函数
        brad.right(10)
    brad.right(90)
    brad.forward(300)
   
    window.exitonclick()#点击窗口自动关闭
draw_art()