#coding=utf-8

# 可以用变量来替代函数
function1=abs;
print(function1(-20))


f=abs;


def function2(x,y,f):
	return f(x)+f(y)

	print(function2(20,10,f))