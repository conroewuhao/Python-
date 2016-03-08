#coding=utf-8 //这行代表代表可以用中文注释



print("多行注释是'''321321321'''类似这样的")

#打印
#单行打印
print("zhe xia wan dan le !");
#多行打印
print("nihao\nwo shi\nwuhao\n");

#指针转向
#a指向abc
a="abc";
#b和a一样指向abc
b=a;
#a指向了hello
a="hello"
#打印b
print(b);

#测试多行注释
"""
fdsfdsafsda
fdsafdsafdsaf
fdsafdsafdsaf
"""

#除法
c=10/3;
print("普通除法得到的c=",10/3);
#地板除
d=10//3;
print("地板除法得到的d=",10//3);
#取余除
e=10%3;
print("取余得到的e=",e);

#字符转化为整数
cd=ord("A");
print("字符的整数表示:",cd);

print(chr(65));
#格式化输出字符串
"""
常见的占位符有：

%d	整数
%f	浮点数
%s	字符串
%x	十六进制整数
其中，格式化整数和浮点数还可以指定是否补0和整数与小数的位数：

>>> '%2d-%02d' % (3, 1)
' 3-01'
>>> '%.2f' % 3.1415926
'3.14'
如果你不太确定应该用什么，%s永远起作用，它会把任何数据类型转换为字符串：

>>> 'Age: %s. Gender: %s' % (25, True)
'Age: 25. Gender: True'
有些时候，字符串里面的%是一个普通字符怎么办？这个时候就需要转义，用%%来表示一个%：

>>> 'growth rate: %d %%' % 7
'growth rate: 7 %'

"""
print("hello,%s,%s"%("wuhao","shijie"))

#更新到http://www.liaoxuefeng.com/wiki/0014316089557264a6b348958f449949df42a6d3a2e542c000/0014316724772904521142196b74a3f8abf93d8e97c6ee6000

