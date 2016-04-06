#coding=utf-8

"""
排序

"""


#简单的从小到大的排序
l=sorted([52,11,22,5,2])
print l


#基于绝对值的比较,key=abs
ll=sorted([-11,-24,-1,2,5,6],key=abs)
print ll


#反序输出,注意关键词reverse
lll=sorted(l,reverse=True)
print lll