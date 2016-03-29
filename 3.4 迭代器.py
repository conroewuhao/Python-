#coding=utf-8

#需要引入相关的头文件
from collections import Iterable
from collections import Iterator

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


"""
可以被next()函数调用并不断返回下一个值的对象称为迭代器：Iterator。

可以使用isinstance()判断一个对象是否是Iterator对象：
"""

print(isinstance(123,Iterator))


"""
小结

凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：
5
"""





