#coding=utf-8

from functools import reduce


#创建一个函数
def f(x):
	return x*x*x

#对可迭代的每一个对象进行函数变换->映射
r=map(str,[1,2,3,4,5,6,7])

print(r)



def add(x,y):
	return x*10+y

"""
再看reduce的用法。reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，
reduce把结果继续和序列的下一个元素做累积计算
"""
r=reduce(add,[2,3,4,5,6])
print(r)
