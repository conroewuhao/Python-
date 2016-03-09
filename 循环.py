#coding=utf-8

#遍历数组进行打印
newArray=["wuhao","ligang","micheal"];
for name in newArray:
	print(name);

#简单的进行计算
a=0;
for x in [1,2,3,4,5,6,7,8,9,10]:
	a+=x;
	print(a);



#简单的求和运算
b=0;
#range(101)代表的意思是[0,1,2,3.......100];
#range()函数可以生成整数数列
for x in range(101):
	b+=x;
	print(b);


newsum=0;
n=0;
while n<100:
	newsum+=n;
	n+=2;

print(newsum);


while 1:
	print("你是一个好人");



