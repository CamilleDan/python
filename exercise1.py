ye# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#基础语法
input("请输入您的身份证号码。")
input("\n评论区")

str = 'Runoob'
 
print (str)          # 输出字符串
print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
print (str[0])       # 输出字符串第一个字符
print (str[2:5])     # 输出从第三个开始到第五个的字符
print (str[2:])      # 输出从第三个开始的后的所有字符
print (str * 2)      # 输出字符串两次
print (str + "TEST") # 连接字符串
print('Ru\noob')
#list
list = [ 'abcd', 786 , 2.23, 'runoob', 70.2 ]
tinylist = [123, 'runoob']
 
print (list)            # 输出完整列表
print (list[0])         # 输出列表第一个元素
print (list[1:3])       # 从第二个开始输出到第三个元素
print (list[2:])        # 输出从第三个元素开始的所有元素
print (tinylist * 2)    # 输出两次列表
print (list + tinylist) # 连接列表

#tuple
tuple=('abc',12,12.3,'dd',True,22.98)
tinytuple=(123,'abf')

print(tuple[2])
print(tuple[2:5])
print(tuple[1:])
print(tuple+tinytuple)
print(tinytuple*2)

vartuple=(1,[2,3],4)
vartuple[1][0]=1
vartuple[1][1]=1
print(vartuple)

#set
student={'tom','rose','alice','tom','tt'}
print(student)
d1=set('afdasdgbsfdasffas')
d2=set('asdfgrteqrdsdasv')
print(d1)
print(d2)
print(d1-d2)
print(d2-d1)
print(d1&d2)
print(d1|d2)
print(d1^d2)
if 'rose' in student:
    print ("rose in student")
else:
    print("rose is not here")

if 'ice' in student:
    print ("ice in student")
else:
    print("ice is not here")

#dictinary
dic={}
dic={'one':'dan','two':'qiao','three':'li'}
print(dic)
print(dic.keys())
print(dic['three'])

#print ("hello,world")
if True:
    print("hello")
else:
    print("oh,no")
    
a,b,c,d=3,3.5,True,4j
print(type(a),type(b),type(c),type(d))
'''
var1=2
var2=3
del var1

print(var2)
'''

var1="Hello,World"
print("var1[0]:",var1[0])
print("var1[1:4]:",var1[1:4])

var2="Run"
print("新加入变量：",var1+","+var2)#加号和逗号不知道有什么区别
print("新加入变量：",var1,var2)
 

print("我要换行!\n","我要换行!\n","我要换行!\n","重要的话说三遍!")


list1=['Hello','World',1,1]
list2=[2,3,4,5]
list3=['a','b','c','d']
print("list1[1]:",list1[1])
print("list1[1:3]:",list1[1:3])
print("list1的第三个元素为：",list1[2])
list1[2]=3
print("更新后list1的第三个元素为：",list1[2])

print("list1:",list1)
del list1[3]
print("new list1:",list1)

#列表脚本操作符
a,b=[1,2,3],[4,5,6]
print("a+b:",a+b)
print("a*4",a*4)
print("3 in a:",3 in a)
print("3 in b:",3 in b)
print("len a:",len(a))
for x in a:
    print(x,end="")

a=[1,2,3]
b=['a','b','c']
x=[a,b]
print(x)
print(x[0])
print(x[0][1])
print(x[1][0])

#迭代
import sys         # 引入 sys 模块
 
list=[1,2,3,4]
it = iter(list)    # 创建迭代器对象
 
while True:
    try:
        print (next(it))
    except StopIteration:
        sys.exit()
 
#define function
def hello():
    print ("hello,world")
hello()          

# computr area
def area(w,h):
    return w*h
def welcome(name):
    print("welcome",name)

w=3
h=4
welcome("dan")
print ("w=",w,"h=",h,"area=",area(w,h))

#date and time
import calendar

cal = calendar.month(2018,9)
print ("以下输出2018年9月份的日历:")
print (cal)
#random package
import random
random.choice(['apple', 'pear', 'banana'])
random.sample(range(100), 10)   # sampling without replacement
random.random()    # random float
random.randrange(6)    # random integer chosen from range(6)

import math
math.cos(math.pi/2)
math.log(1024, 2)


