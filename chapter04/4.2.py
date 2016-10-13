#本文件主要讨论python迭代器的使用

#一般来讲，迭代器iter方法一般会返回自身，这保证了是一个可迭代的对象，出现在for语句之中
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
        return self
print("myIterators")
Iterators = myiter()
a=[num for num in Iterators]
b=[num for num in Iterators]
print(a)
print(b)
#这是因为迭代器完成之后继续使用了self自身，而self自身已经达到了结尾，这里也有一种解决方案，就是返回一个自身的实例，可能会消耗内存一些
print("IteratorA")
Iterators = IteratorA()
a=[num for num in Iterators]
b=[num for num in Iterators]
print(a)
print(b)


#注意一般的含有yeild的函数类型是什么是GeneratorType，这种类型是含有iter定义的，而且返回自身因此可以for中出现
def test_gen():
    k = 1
    while k < 3:
        yield k
        k += 1

print("test_Gen")
Iterators = test_gen()
a=[num for num in Iterators]
b=[num for num in Iterators]
print(a)
print(b)


#如果将这两种结合起来会发生什么
class IterGen:
    def __init__(self):
        self.start = 5

    def __iter__(self):
        while self.start < 10:
            self.start += 1
            yield self.start

print("IterGen")
Iterators = IterGen()
a=[num for num in Iterators]
b=[num for num in Iterators]
print(a)
print(b)

#解释，因为for语句的功能是：接受一个可以迭代的对象就是有iter函数的对象，然后隐式的产生一个迭代器，然后对这个迭代器
#调用next进行迭代
#yield语句可以理解为，产生一个generator的对象，这个对象的iter能够返回自身
#因此iterGen()产生的是一个可以迭代的对象
#The for loop only expects the object returned by __iter__ to have a __next__ method. 
#The __iter__ method is a generator function because of the yield statement in the body.
# Therefore, when __iter__ is called, it returns a generator object, which you can call __next__ on.
#通过实验发现，这种也是不能持续使用的类型

#这里我们可以发现.....含有yeild的语句的都是GenneratorType，因此传进for语句的是一个class的话，会根据情况产生迭代器，
#(这里传入的是是一个generator，但是我们可以直接对这个对象调用next
#如果传入for语句的是Generator的类型的话，也会对这个类型调用迭代器_iter_但是这里的_iter_恰好又是自身




#getitem也能创建迭代器，如何创建？
class arange():
    def __init__(self,lo,hi):
        self.lo=lo
        self.hi=hi
    def __len__(self):
        return max(self.lo, self.hi) - min(self.lo, self.hi)
    def __getitem__(self,k):
        if k < 0:
            k = len(self) - k#这里一定要处理负数的情况才行
        if 0 <= k < len(self):
            return self.lo + k
        else:
            raise IndexError
            
print("Range")
Iterators = arange(1,4)
a=[num for num in Iterators]
b=[num for num in Iterators]
print(a)
print(b)


# Extra Questions

# Q8
def scale(s, k):
    """Yield elements of the iterable s scaled by a number k.

    >>> s = scale([1, 5, 2], 5)
    >>> type(s)
    <class 'generator'>
    >>> list(s)
    [5, 25, 10]

    >>> m = scale(naturals(), 2)
    >>> [next(m) for _ in range(5)]
    [2, 4, 6, 8, 10]
    """
    ss= iter(s)

    index = next(ss)
    while True:
        yield index * k
        index = next(ss)


    
# Q9
def merge(s0, s1):
    """Yield the elements of strictly increasing iterables s0 and s1, removing
    repeats. Assume that s0 and s1 have no repeats. You can also assume that s0
    and s1 represent infinite sequences.

    >>> twos = scale(naturals(), 2)
    >>> threes = scale(naturals(), 3)
    >>> m = merge(twos, threes)
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [2, 3, 4, 6, 8, 9, 10, 12, 14, 15]
    """
    i0, i1 = iter(s0), iter(s1)
    e0, e1 = next(i0), next(i1)
    while True:
        if e0 == e1:
            yield e0
            e0 = next(i0)
            e1 = next(i1)
        elif e0 < e1:
            yield e0
            e0 = next(i0)
        else:
            yield e1
            e1 = next(i1)


# Q10
def remainders_generator(m):
    """
    Takes in an integer m, and yields m different remainder groups
    of m.

    >>> remainders_mod_four = remainders_generator(4)
    >>> for rem_group in remainders_mod_four:
    ...     for _ in range(3):
    ...         print(next(rem_group))
    0
    4
    8
    1
    5
    9
    2
    6
    10
    3
    7
    11
    """

    k = -1
    while k<m:
        k += 1
        def gf():#其实这个并不像函数，
            current = k
            while True:
                yield current
                current += m
        yield gf()#这里为什么不能是函数，而是函数的对象，

# the naturals generator is used for testing scale and merge functions
def naturals():
    """A generator function that yields the infinite sequence of natural
    numbers, starting at 1.

    >>> m = naturals()
    >>> type(m)
    <class 'generator'>
    >>> [next(m) for _ in range(10)]
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    """
    i = 1
    while True:
        yield i
        i += 1

# Q11
def zip(*iterables):
    """
    Takes in any number of iterables and zips them together. 
    Returns a generator that outputs a series of lists, each 
    containing the nth items of each iterable. 
    >>> z = zip([1, 2, 3], [4, 5, 6], [7, 8])
    >>> for i in z:
    ...     print(i)
    ...
    [1, 4, 7]
    [2, 5, 8]
    """
    #传入的对象是可以迭代的，但是不是迭代器，我们生成迭代器
    iters = [ iter(item) for item in iterables]
    while True:
        yield [ next(elem) for elem in iters]


print('test_cases_for_extra_questions')
print(list(scale([1,2,3],4)))
twos = scale(naturals(), 2)
threes = scale(naturals(), 3)
m = merge(twos, threes)
print(next(m))
print(next(m))

remainders_mod_four = remainders_generator(4)
for rem_group in remainders_mod_four:#在这里加上也不行，生成器的对象要求是不能call的
    for _ in range(3):
        print(next(rem_group))

z = zip([1, 2, 3], [4, 5, 6], [7, 8])
for i in z:
    print(i)

########################################################

class Stream:
    """A lazily computed linked list."""
    class empty:
        def __repr__(self):
            return 'Stream.empty'
    empty = empty()
    def __init__(self, first, compute_rest=lambda: empty):
        assert callable(compute_rest), 'compute_rest must be callable.'
        self.first = first
        self._compute_rest = compute_rest
    @property
    def rest(self):
        """Return the rest of the stream, computing it if necessary."""
        if self._compute_rest is not None:
            self._rest = self._compute_rest()
            self._compute_rest = None
        return self._rest
    def __repr__(self):
        return 'Stream({0}, <...>)'.format(repr(self.first))


def integer_stream(first):
    def compute_rest():
        return integer_stream(first+1)
    return Stream(first, compute_rest)


def map_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return map_stream(fn, s.rest)
    return Stream(fn(s.first), compute_rest)

def filter_stream(fn, s):
    if s is Stream.empty:
        return s
    def compute_rest():
        return filter_stream(fn, s.rest)
    if fn(s.first):
        return Stream(s.first, compute_rest)
    else:
        return compute_rest()



