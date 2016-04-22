#coding=utf-8

"""
Python的functools模块提供了很多有用的功能，其中一个就是偏函数（Partial function）。
要注意，这里的偏函数和数学意义上的偏函数不一样。

在介绍函数参数的时候，我们讲到，通过设定参数的默认值，可以降低函数调用的难度。
而偏函数也可以做到这一点。举例如下：

"""

import functools


#定义一个可以转化2进制的函数
int2=functools.partial(int,base=2)
print int2('1010101101')

#functools.partial的作用就是，把一个函数的某些参数固定住,然后返回一个新的函数