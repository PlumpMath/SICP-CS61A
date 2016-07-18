
class Countdown:
    """
    >>> from types import GeneratorType
    >>> type(Countdown(0)) is GeneratorType # Countdown is an iterator
    False
    >>> for number in Countdown(5):
    ...     print(number)
    ...
    5
    4
    3
    2
    1
    0
    """
    def __init__(self,begin):
        self.begin = begin
    def __iter__(self):
        while self.begin > 0:
            yield self.begin
            self.begin -= 1



#返回自身的迭代器

class myiter():
    def __init__(self):
        self.now = 1
        self.lo = 1
        self.hi = 10
    def __iter__(self):
        return self
    def __next__(self):
        if self.now <= self.hi:
            self.now += 1
            return self.now-1
        else:
            raise StopIteration



class IteratorA:
    def __init__(self):
        self.mark = 10
        self.start = 10

    def __next__(self):
        if self.start > 100:
            raise StopIteration
        self.start += 20
        return self.start

    def __iter__(self):
        self.start = self.mark
        #或者建立一个新的对象
        return self




#如果将这两种结合起来会发生什么
class IterGen:
    def __init__(self):
        self.start = 5

    def __iter__(self):
        while self.start < 10:
            self.start += 1
            yield self.start

for i in IterGen():
    print(i)

#解释，因为for语句的功能是：接受一个可以迭代的对象就是有iter函数的对象，然后隐式的产生一个迭代器，然后对这个迭代器
#调用next进行迭代，
#yield语句可以理解为，产生一个generator的对象，这个对象的iter能够返回自身
#因此iterGen()产生的是一个可以迭代的对象

#The for loop only expects the object returned by __iter__ to have a __next__ method. 
#The __iter__ method is a generator function because of the yield statement in the body.
# Therefore, when __iter__ is called, it returns a generator object, which you can call __next__ on.


from types import GeneratorType
print(type(iter(Countdown(0))) is GeneratorType)

#这里我们可以发现.....含有yeild的语句的都是GenneratorType，因此传进for语句的是一个class的话，会根据情况产生迭代器，
#(这里传入的是是一个generator，但是我们可以直接对这个对象调用next
#如果传入for语句的是Generator的类型的话，也会对这个类型调用迭代器_iter_但是这里的_iter_恰好又是自身



