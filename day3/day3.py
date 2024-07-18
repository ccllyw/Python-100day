'''

可以使用if...elif...else...结构或者嵌套的if...else...结构


练习2：百分制成绩转换为等级制成绩。
要求：如果输入的成绩在90分以上（含90分）输出A；80分-90分（不含90分）输出B；70分-80分（不含80分）输出C；60分-70分（不含70分）输出D；60分以下输出E。
f = int(input('请输入分数：'))
if f >= 90:
    print('A')
elif 80 <= f < 90:
    print('B')
elif 70 <= f < 80:
    print('C')
elif 60 <= f < 70:
    print('D')
else:
    print('E')



百分制成绩转换为等级制成绩

Version: 0.1
Author: 骆昊

score = float(input('请输入成绩: '))
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
elif score >= 60:
    grade = 'D'
else:
    grade = 'E'
print('对应的等级是:', grade)
'''

"""
判断输入的边长能否构成三角形，如果能则计算出三角形的周长和面积

Version: 0.1
Author: 骆昊

a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
if a + b > c and a + c > b and b + c > a:
    print('周长: %f' % (a + b + c))
    p = (a + b + c) / 2
    area = (p * (p - a) * (p - b) * (p - c)) ** 0.5
    print('面积: %f' % (area))
else:
    print('不能构成三角形')
print('请输入三角形三边长度')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
s = (a + b + c ) / 2
if a + b > c and a + c > b and b + c > a:
    print(f'周长为：{a + b+ c},面积为：{(s*(s -a)*(s - b)*(s - c)) ** 0.5}')
else:
    print('不能构成三角形')

"""