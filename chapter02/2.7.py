
##########################################################
from math import atan2,cos,sin,pi
#面向对象中的设计模式-实现复数和分数的运算
#首先定义一个数的抽象类
class Number():
    def __add__(self, another):
        return self.add(another)
    def __mul__(self, another):
        return self.mul(another)

#############
#这是后期实现
#############
def add_rational_and_complex(r,c):
    return ComplexRI(c.real + r.b / r.a, c.imag)
def add_complex_and_rational(c,r):
    return add_rational_and_complex(r,c)


class Number():
    adders_relation = { ('com','rat') : add_complex_and_rational, ('rat','com') : add_rational_and_complex }
    def __add__(self, another):
        if self.tag == another.tag:
            return self.add(another)
        #首先要注意各种self必须加上，因为后面继承的对象可能如果使用adders_relation一定要用到self，并不像C++一样
        elif (self.tag, another.tag) in self.adders_relation:
            #第二这样是不能索引字典的
            fn = self.adders_relation[(self.tag, another.tag)]
            return fn(self, another)
    def __mul__(self, another):
        if self.tag == another.tag:
            return self.mul(another)
        #实现和add类似
        
    
#然后定义一个复数的抽象类，继承自Number
class Complex(Number):
    def add(self, another):
        return ComplexRI(self.real + another.real, self.imag + another.imag)
    def mul(self,another):
        return ComplexMA(self.dis * another.dis, self.ang + another.ang)
#分别定义两种类型
class ComplexRI(Complex):
    def __init__(self, x, y):
        self.real = x
        self.imag = y
    @property
    def dis(self):
        return (self.real**2 + self.imag**2)**0.5
    @property
    def ang(self):
        return atan2(self.imag, self.real)
    def __str__(self):
        return 'ComplexMA({0:g},{1:g})'.format(self.real, self.imag)
class ComplexMA(Complex):
    def __init__(self, dis, ang):
        self.dis = dis
        self.ang = ang
    @property
    def imag(self):
        return self.dis * sin(self.ang)
    @property
    def real(self):
        return self.dis * cos(self.ang)
    def __str__(self):
        return 'ComplexMA({0:g},{1:g}*pi)'.format(self.dis, self.ang/pi)

#面向对象的程序设计，制作一个分数
from fractions import gcd
class Ration(Number):
    def __init__(self, a, b):#a分母b分子
        g = gcd(a, b)
        self.a = a // g
        self.b = b // g
    def add(self, another):
        a1, b1 = self.a, self.b
        a2, b2 = another.a, another.b
        return Ration(a1 * a2, b1 * a2 + b2 * a1)
    def mul(self, another):
        return Ration(self.a*another.a, self.b*another.b)
    def __str__(self):
        return 'Ration({0:g},{1:g})'.format(self.b, self.a)

#检测类型可以使用
#print(isinstance())

#我们可以加标签来实现rational和complex之间的加法和乘法
Ration.tag = 'rat'
Complex.tag = 'com'

#具体实现见上面“后期实现”



####测试####
ma = ComplexMA(2, pi / 2)
print(ma)
ri = ComplexRI(1, 2)
print(ri)
print(ri + ma)
tar = ri * ma
print(tar)
print(tar.real)
print(tar.imag)

zhang = Ration(1, 2)
tar = ri + zhang
print(tar)