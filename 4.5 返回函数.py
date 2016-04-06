#coding=utf-8

def lazy_sum(*args):
    def sum():
        ax = 0
        for n in args:
            ax = ax + n
        return ax
    return sum


"""
当我们调用lazy_sum()时，返回的并不是求和结果，而是求和函数：

"""
f=lazy_sum(1,2,3,4,5,6)
print f

"""
f()是执行求和函数
"""
print f()



"""
注意闭包函数

全部都是9！原因就在于返回的函数引用了变量i，但它并非立刻执行。等到3个函数都返回时，它们所引用的变量i已经变成了3，因此最终结果为9。

返回闭包时牢记的一点就是：返回函数不要引用任何循环变量，或者后续会发生变化的变量。
"""
def count():
	fs=[]
	for i in range(1,4):
		def f():
			return i*i
		fs.append(f)
	return fs

f1,f2,f3=count()

print f1()

"""


"""

def countnew():
    def f(j):
        def g():
            return j*j
        return g
    fs = []
    for i in range(1, 4):
        fs.append(f(i)) # f(i)立刻被执行，因此i的当前值被传入f()
    return fs


f4,f5,f6=countnew()
print f4()
print f5()
print f6()


