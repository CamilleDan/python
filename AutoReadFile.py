# -*- coding: utf-8 -*-
"""
Created on Thu Aug 23 16:17:09 2018

@author: windows7
"""

import os,time#引用模块
s=["杨丹","方竟先","勤奋努力每一天"]#定义列表字符串
fn=r"e:/demo/demo.txt"#路径赋给变量，便于调用

def write():#写文件的函数
    a=open(fn,"w")#open方法打开文件，权限为写入
    a.write("杨丹！方竟先！勤奋努力每一天！")#写入内容
    a.close()#关闭文件
    print("未找到文件，已写入文件")

def read():#读文件函数
    a=open(fn,"r").read()#读取内容
    return a
    
def fix():
    a=open(fn,"w")
    a.write("杨丹！方竟先！勤奋努力每一天！")
    a.close()
    print("文件被篡改，已恢复")
    
if os.path.exists(fn):#判断文件是否存在
    z=read()
    #print(z.find(s[1]))查看读取内容
    if z.find(s[0])!=-1 & z.find(s[1])!=-1:#find参数为要寻找的字符串
        print("关键字均存在")
    else:
        fix()
else:
    write()
    