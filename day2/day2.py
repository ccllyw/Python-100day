"""
:type及变量类型


a = 1
b = 1.1
c = "你好"
d = 1 + 2j
e = True

print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))

int()：将一个数值或字符串转换成整数，可以指定进制。
float()：将一个字符串转换成浮点数。
str()：将指定的对象转换成字符串形式，可以指定编码。
chr()：将整数转换成该编码对应的字符串（一个字符）。
ord()：将字符串（一个字符）转换成对应的编码（整数）

a = int(input('a = '))
#int()转化为整型
b = int(input('b = '))
print('%d + %d = %d' % (a, b, a + b))
print('%d / %d = %f' % (a, b, a / b))
print('%d // %d = %d' % (a, b, a // b))
print('%d ** %d = %d' % (a, b, a ** b))
上面的print函数中输出的字符串使用了占位符语法，其中%d是整数的占位符，%f是小数的占位符，%%表示百分号（因为百分号代表了占位符，
所以带占位符的字符串中要表示百分号必须写成%%），字符串之后的%后面跟的变量值会替换掉占位符然后输出到终端中，运行上面的程序，看看程序执行结果就明白啦


a = 5
b = 10
a += b
# a = a + b
a *= b + 2
# a = a * (b + 2)

运算符	描述
[] [:]	下标，切片
**	指数
~ + -	按位取反, 正负号
* / % //	乘，除，模，整除
+ -	加，减
>> <<	右移，左移
&	按位与
^ |	按位异或，按位或
<= < > >=	小于等于，小于，大于，大于等于
== !=	等于，不等于
is is not	身份运算符
in not in	成员运算符
not or and	逻辑运算符
= += -= *= /= %= //= **= &= `	= ^= >>= <<=`


flag0 = 1 == 1
flag1 = 3 > 2
flag2 = 2 < 1
flag3 = flag1 and flag2
# 有一个false就是False
flag4 = flag1 or flag2
# 有一个True就是True
flag5 = not (1 != 2)
print('flag0 =', flag0)    # flag0 = True
print('flag1 =', flag1)    # flag1 = True
print('flag2 =', flag2)    # flag2 = False
print('flag3 =', flag3)    # flag3 = False
print('flag4 =', flag4)    # flag4 = True
print('flag5 =', flag5)    # flag5 = False

输入℉转为℃

h = int(input('请输入华氏温度：'))
s = (h - 32) / 1.8
print('%d华氏温度 = %d摄氏温度' % (h, s))

f = float(input('请输入华氏温度: '))
c = (f - 32) / 1.8
print('%.2f华氏度 = %.2f摄氏度' % (f, c))
print(f'{f:.1f}华氏度 = {c:.1f}摄氏度')
# %占位符，%f浮点值，.2保留2位小数
# f‘{}’也是占位符


r = int(input('请输入圆的半经：'))
p = 3.1415926
s = 2 * r * p
m = r ** 2 * p
print(f'圆的面积是：{m}圆的周长是：{s}')

radius = float(input('请输入圆的半径: '))
perimeter = 2 * 3.1416 * radius
area = 3.1416 * radius * radius
print('周长: %.2f' % perimeter)
print('面积: %.2f' % area)


n = int(input('请输入年份：'))
m = n // 4 and n // 100 and
"""
# 测试本地仓库推送至远程仓库
# 测试2