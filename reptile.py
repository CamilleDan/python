# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 08:40:52 2018

@author: windows7
"""
#方法1
import urllib2
#直接请求
response=urllib2.urloppen("")

#获取状态码，200表示成功
print (response.getcode())

#读取内容
cont=response.read()


#方法2
import urllib2
#创建Request对象
request=urllib2.Request(url)