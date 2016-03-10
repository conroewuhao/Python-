#coding=utf-8

#自定
def testfunction(x):
	return -x

a=testfunction(2919)
print(a)

#自定义函数2
def function2(numbers):
	a=0
	for n in numbers:
		a=a+n*n
	return a	

b=function2([1,2,3,4])
print(b)


#关键字参数,**代表可以省略的参数
def guanjianzifunction(name,age,**height):
	print("name",name,"age",age,"other",height)


guanjianzifunction("wuhao",20)
guanjianzifunction("micheal",14)
guanjianzifunction("wuhao",14,city="hefei")


#可以利用**来获取更多参数(以字典的方式)
extra={"city":"beijing","weight":"20"}
guanjianzifunction("wuhao",14,**extra)


#可以利用*来取得Tuple参数
def completefunction(name,age,*height,**other):
	print("name:",name,"age:",age,"height:",height,"other",other)

extranew={"jionghao":123,"buzhidao":421}
completefunction("wuhao",12,144,123,124,**extranew)





