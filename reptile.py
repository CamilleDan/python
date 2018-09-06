# -*- coding: utf-8 -*-
"""
Created on Tue Aug  7 08:40:52 2018

@author: windows7
"""
#方法1
from urllib import request
import re#使用正则表达式

def getResponse(url):
    #请求对象Request是一个类
    url_request=request.Request(url)
    url_response=request.urlopen(url_request)
    
    return url_response
#直接请求获取网页内容，将内容赋予response对象

def getJpg(data):
    jpglist=re.findall(r'src="http.+?.jpg"',data)
    return jpglist

def downLoad(jpgUrl,n):
    try:
        request.urlretrieve(jpgUrl,'%s.jpg' %n)
    except Exception as e:
        print(e)
    finally:
        print('图片%s下载操作完成' %n)
        

http_response=getResponse('https://www.douban.com/')
data=http_response.read().decode('utf-8')

global n
n=1
L=getJpg(data)
for jpginfo in L:
    print(jpginfo)
    s=re.findall(r'src="http.+?.jpg"',jpginfo)
    downLoad(s[0],n)
    n=n+1