# encoding:utf-8

import os

lll=[]
for n in range(0,10):
	lll.append(n*n)
print(lll)

#创建有条件的list
haha=[x*x*x for x in range(0,20)]
print(haha)

#两层循环
wuhao=[m+n for m in "abc" for n in "xwz"]
print(wuhao)

#遍历出目录中的文件
print([d for d in os.listdir(".")])
