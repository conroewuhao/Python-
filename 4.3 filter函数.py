#coding=utf-8


#定义一个筛选函数

def is_odd(n):
    return n % 2 == 0

#使用filter函数可以进行筛选
llll=filter(is_odd,[1,2,3,4,5,67])
print(llll)


def exceptemptychar(s):
	return s and s.strip()


lll=filter(exceptemptychar,['2',"da","","","sagds","gd"])
print(lll)


"""
Python求素数的方法

"""
def getPrime(maxNum):
    aList = [x for x in range(0,maxNum)]
    prime = []
    for i in range(2,len(aList)):
        if aList[i] != 0:
            prime.append(aList[i])
            clear(aList[i],aList,maxNum)
    return prime
      
def clear(aPrime,aList,maxNum):
    for i in range(2,int((maxNum/aPrime)+1)):
        if not aPrime*i>maxNum-1:
            aList[i*aPrime]=0

print getPrime(100)





