#coding=utf-8


#使用()产生生成器
g=(x*x for x in range(100))
print(g)

#遍历生成器的每个元素
for n in g:
	print(n)

#定义菲波那切数列
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        print(b)
        a, b = b, a + b
        n = n + 1
    return 'done'

#测试菲波那切数列
fib(12)

#定义杨辉三角
def triangles():
    N=[1]
    while True:
        yield N
        #补0
        N.append(0)
        N=[N[i-1]+N[i] for i in range(len(N))]

#测试杨辉三角
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break

