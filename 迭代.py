#coding=utf-8

#方法是通过collections模块的Iterable类型判断
from collections import Iterable

#迭代

#建立字典
d={"a":1,"b":2,"c":3}

#遍历打印值
for value in d.values():
	print(value)


#遍历打印key
for key in d:
	print(key)


#判断是否迭代
print(isinstance(d,Iterable));
print(isinstance([1,2,3],Iterable))

#类似Java的同时取得下标和值,注意enumerate的写法
for x,y in enumerate(["a","b","c"]):
          print(x,y)

