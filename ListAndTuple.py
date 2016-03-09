#coding:utf-8

"""
List对象可以保存不同的数据类型,List理解为可变数组

"""

classmates=["lily","wanger","ligang"];
#打印数组的某个元素
print("数组的第二个元素是:%s" % (classmates[1]));

#打印数组长度
print("数组的长度是%d" % (len(classmates)));
print(len(classmates));

#在某个位置插入元素
classmates.insert(1,'wuhao');

print("now newlistlength:%d" % (len(classmates)));

print(classmates);

#在某个位置弹出元素
classmates.pop(0);
print(classmates);

#List对象可以保存不同的数据类型,注意Python是大小写敏感
newList1=["true",True,123];
print(newList1);

#IndexError: list index out of range
#print(classmates[5]);


"""
Tuple理解为不可变数组

"""

tuple1=("wuhao","ligang","wanglei");

print("不可变数组第一个元素是:%s" % (tuple1[0]));

tuple1.insert(1,"abc");
print(tuple1);



