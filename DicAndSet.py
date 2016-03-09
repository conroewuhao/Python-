#coding=utf-8


"""
字典的相关操作
"""


#定义一个字典
dic={"wuhao":8,"micheal":9}
#根据key进行打印
print(dic["wuhao"]);


#判断是否存在key
hasornot=dic.has_key("micheal")
print(hasornot)

#对应的key
key=dic.get("micheal");
print(key);


#删除key
dic.pop("micheal");
print(dic);

"""
请务必注意，dict内部存放的顺序和key放入的顺序是没有关系的。

和list比较，dict有以下几个特点：

查找和插入的速度极快，不会随着key的增加而变慢；
需要占用大量的内存，内存浪费多。
而list相反：

查找和插入的时间随着元素的增加而增加；
占用空间小，浪费内存很少。
所以，dict是用空间来换取时间的一种方法。

dict可以用在需要高速查找的很多地方，在Python代码中几乎无处不在，正确使用dict非常重要，需要牢记的第一条就是dict的key必须是不可变对象。

"""

"""
集合操作
set和dict类似，也是一组key的集合，但不存储value。由于key不能重复，所以，在set中，没有重复的key。

"""
#初始化一个set,自动过滤重复的key
s=set([1,2,3,4,5,6,2,4]);
print(s)

#添加一个key
s.add(10);
print(s);

#a指向的是不可变的字符串abc
"""
当我们调用a.replace('a', 'A')时，实际上调用方法replace是作用在字符串对象'abc'上的，
而这个方法虽然名字叫replace，但却没有改变字符串'abc'的内容。相反，replace方法创建了一个新字符串'Abc'并返回，
如果我们用变量b指向该新字符串，就容易理解了，变量a仍指向原有的字符串'abc'，但变量b却指向新字符串'Abc'了：

"""
a='abc'
b=a.replace('a','A')
print(b)
print(a)


