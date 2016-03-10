#coding=utf-8

#注意Python缩进的格式

#菲波那切数列的函数表达式
def diguifunction(n):
  if n==1:
    return 1
  return n*diguifunction(n-1)

a=diguifunction(5)
print(a)
print(a.bit_length())

#递归的思路解决汉罗塔
def move(n,a,b,c):
	if n==1:
		print("这步%s---%s" %(a,c))
	else:
		#n-1柱子从a->b
	    move(n-1,a,c,b)
	    #剩下的柱子从a->c
	    move(1,a,b,c)
	    #让b上的n-1柱子搬到c
	    move(n-1,b,a,c)	

move(18,'a','b','c')