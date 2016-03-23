#coding=utf-8

#需要引入相关的头文件
from collections import Iterable

#判断字符串是否可以迭代
print(isinstance("sbc",Iterable))
#判断列表是否可以迭代
print(isinstance([],Iterable))
#判断字典是否可以迭代
print(isinstance({},Iterable))

#判断数字是否可以迭代
print(isinstance(123,Iterable))

#判断一个循环是否可以迭代
print(isinstance((x for x in range(10)),Iterable))
