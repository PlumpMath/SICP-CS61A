from operator import add, sub
from operator import mul, truediv

#制作一个容器
def make_ternary_constraint(a, b, c, ab, ca, cb):
    """The constraint that ab(a,b)=c and ca(c,a)=b and cb(c,b) = a."""
    def new_value():
        #判断连接器是否有变量，将有变量的全部计算出来，放到链接器中的变量中去
        av, bv, cv = [connector['has_val']() for connector in (a, b, c)]#a,b,c是三个的连接器
        if av and bv:
            c['set_val'](constraint, ab(a['val'], b['val']))
        elif av and cv:
            b['set_val'](constraint, ca(c['val'], a['val']))
        elif bv and cv:
            a['set_val'](constraint, cb(c['val'], b['val']))

    def forget_value():
        #容器下达指令让所有与之相关的连接器的内容清零
        for connector in (a, b, c):
            connector['forget'](constraint)
    ##########################################################
    constraint = {'new_val': new_value, 'forget': forget_value}
    ##########################################################
    for connector in (a, b, c):
        connector['connect'](constraint)

    return constraint


def multiplier(a, b, c):
    """The constraint that a * b = c."""
    return make_ternary_constraint(a, b, c, mul, truediv, truediv)
def adder(a, b, c):
    """The constraint that a + b = c."""
    return make_ternary_constraint(a, b, c, add, sub, sub)



#是容器，常量容器
def constant(connector, value):
    """The constraint that connector = value."""
    constraint = {}
    connector['set_val'](constraint, value)#将连接器的变量置为常数
    return constraint#返回一个常量容器

def connector(name=None):#连接器
    """A connector between constraints."""
    informant = None
    constraints = []#存放一个字典的列表集合，表示有哪些容器，而且这些容器可以下达什么指令

    def set_value(source, value):
        nonlocal informant#记忆上一次下达指令的源
        val = connector['val']
        if val is None:#如果原来
            informant, connector['val'] = source, value
            if name is not None:
                print(name, '=', value)
            inform_all_except(source, 'new_val', constraints)
        else:
            if val != value:
                print('Contradiction detected:', val, 'vs', value)

    def forget_value(source):
        nonlocal informant#记忆上一次下达指令的源
        if informant == source:
            informant, connector['val'] = None, None
            if name is not None: #如果连接器的名字不是空的，那么就显示已经清零
                print(name, 'is forgotten')
            inform_all_except(source, 'forget', constraints)#调用通知函数，告知和这一个链接器相连的容器

    connector = {'val': None,#连接器的变量
                 'set_val': set_value,
                 'forget': forget_value,
                 'has_val': lambda: connector['val'] is not None,
                 'connect': lambda source: constraints.append(source)}#将相连的容器加上一个容器（源）
    return connector


#这里的souce一直以来就是一个字典，前半部分存放着信息，后半部分存放着信息对应的函数，这里的constrain是souce的集合也就是
#因此抽象出来：容器是souce的集合

def inform_all_except(source, message, constraints):
    #除了特定的souce之外
    """Inform all constraints of the message, except source."""
    #调用容器中的特定信息
    for c in constraints:
        if c != source:
            c[message]()



#快速建立本例的测试样例之间的关系
def converter(c, f):
    """Connect c to f with constraints to convert from Celsius to Fahrenheit."""
    u, v, w, x, y = [connector() for _ in range(5)]
    multiplier(c, w, u)
    multiplier(v, x, u)
    adder(v, y, f)

    constant(w, 9)
    constant(x, 5)
    constant(y, 32)


celsius = connector('Celsius')
fahrenheit = connector('Fahrenheit')
converter(celsius, fahrenheit)
celsius['set_val']('user', 25)

########################################################
#nonlocal规则
#python是不允许多个函数同时修改全局变量的，这是python3的新规定，为了降低多个模块之间的耦合性

def function(x):   
    a = 100
    def fun1(x1):
        nonlocal a
        a = a - x1
        return a
    def fun2(x2):
        nonlocal a
        a = a + x2
        return a
    if x == 1:
        return fun1
    else:
        return fun2
fx = function(1)
print(fx(5))
print(fx(5))
gx = function(2)
print(gx(10))
###############################################
#例子
def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance
        if amount > balance:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

wd = make_withdraw(20)
wd2 = make_withdraw(7)
wd2(6)
wd(8)
################################################
def function(a):
    def x():
        nonlocal a
        #注意如果是a = 4就不会报错，因为编译器认为又在这个frame增加了一个变量是a
        a = a - 4
        return a
    return x



####但是如果是字典呢
def function2():
    dic = {}#为什字典是可以修改局部变量的，大概是因为字典存放的是指针吧
    def inside():
        dic['zhanglanqing'] = 1
        return dic['zhanglanqing']
    return inside