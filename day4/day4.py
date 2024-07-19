# 循环结构
'''

如果明确的知道循环执行的次数或者要对一个容器进行迭代（后面会讲到），那么我们推荐使用for-in循环

求1-100的和


sum = 0
for x in range(101):
    sum += x
print(sum)


range(101)：可以用来产生0到100范围的整数，需要注意的是取不到101。
range(1, 101)：可以用来产生1到100范围的整数，相当于前面是闭区间后面是开区间。
range(1, 101, 2)：可以用来产生1到100的奇数，其中2是步长，即每次数值递增的值。
range(100, 0, -2)：可以用来产生100到1的偶数，其中-2是步长，即每次数字递减的值。


用for循环实现1~100之间的偶数求和



sum = 0
for x in range(0,101,2):
    sum += x
print(sum)

------------------------------------

如果要构造不知道具体循环次数的循环结构，我们推荐使用while循环。while循环通过一个能够产生或转换出bool值的表达式来控制循环，表达式的值为True则继续循环；表达式的值为False则结束循环

猜数字游戏


import random

s = random.randint(1,1000)
couter = 0
while True:
    couter += 1
    n = int(input('请输入你猜的数字：'))
    if n > s:
        print('大了一点')
    elif n < s:
        print('小了一点')
    else:
        print('恭喜你猜对了')
        break
print(f'你共猜了{couter}次')
if couter < 20 :
    print('你是个天才')


上面的代码中使用了break关键字来提前终止循环，需要注意的是break只能终止它所在的那个循环，这一点在使用嵌套的循环结构（下面会讲到）需要引起注意。除了break之外，还有另一个关键字是continue，它可以用来放弃本次循环后续的代码直接让循环进入下一轮。


输出乘法口诀表(九九表)


for i in range(1,10):
    for j in range(1,i+1):
        print(f'{i} * {j} = {i * j}',end='\t')
    print()

python 打印后会默认一个换行符，end可以自定义结尾
--------------------------------------------------------------------
练习1：输入一个正整数判断是不是素数。
提示：素数指的是只能被1和自身整除的大于1的整数


n = int(input('请输入正整数：'))
if n == 1:
    print(f'{n}不是素数')
else:
    for i in range(2,n):
        if n % i == 0:
            print(f'{n}不是素数')
            break
        else:
            print(f'{n}是素数')
            break


from math import sqrt

num = int(input('请输入一个正整数: '))
end = int(sqrt(num))
is_prime = True
for x in range(2, end + 1):
    if num % x == 0:
        is_prime = False
        break
if is_prime and num != 1:
    print('%d是素数' % num)
else:
    print('%d不是素数' % num)
------------------------------------------------------------------------------------------------------------
练习2：输入两个正整数，计算它们的最大公约数和最小公倍数。
提示：两个数的最大公约数是两个数的公共因子中最大的那个数；两个数的最小公倍数则是能够同时被两个数整除的最小的那个数。



n = int(input('请输入第一个数：'))
m = int(input('请输入第二个数：'))
if n > m:
    n, m = m, n
for x in range(m+1, 0, -1):
    if n % x ==0 and m % x == 0:
        print(f'最大公约数是{x}')
        print(f'最小公倍数是{(n * m) // x}')
        break

x = int(input('x = '))
y = int(input('y = '))
# 如果x大于y就交换x和y的值
if x > y:
    # 通过下面的操作将y的值赋给x, 将x的值赋给y
    x, y = y, x
# 从两个数中较小的数开始做递减的循环
for factor in range(x, 0, -1):
    if x % factor == 0 and y % factor == 0:
        print('%d和%d的最大公约数是%d' % (x, y, factor))
        print('%d和%d的最小公倍数是%d' % (x, y, x * y // factor))
        break

 '''

"""
打印三角形图案

Version: 0.1
Author: 骆昊
"""

row = int(input('请输入行数: '))
for i in range(row):
    for _ in range(i + 1):
        print('*', end='')
    print()


for i in range(row):
    for j in range(row):
        if j < row - i - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()

for i in range(row):
    for _ in range(row - i - 1):
        print(' ', end='')
    for _ in range(2 * i + 1):
        print('*', end='')
    print()


# 打印三角形未作，很有意思有时间再学习回顾时做






