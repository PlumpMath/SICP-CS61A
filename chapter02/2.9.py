#使用类的泛化的方法优雅的实现各种数据结构

class Link():
    empty = ()#空的元组
    def __init__(self, fir, res=empty):
        assert res is Link.empty or isinstance(res, Link)
        self.fir = fir
        self.res = res
    def __getitem__(self, index):
        if index == 0:
            return self.fir
        else:
            if self.res == Link.empty:
                return -1
            else:
                return self.res.__getitem__(index - 1)
    def __len__(self):
        return 1 + self.res.__len__()
   
    def __repr__(self):
        #通过回溯的过程中确定表达的类型
        if self.res == Link.empty:
            res =  ' '
        else:
            res =  '+' + self.res.__repr__()
        return 'Link({0},{1})'.format(self.fir, self.res)

    def __add__(self, t):
            if self.res is Link.empty:
                return Link(self.fir, t)
            else:
                return Link(self.fir, self.res.__add__(t))

def map_link(f, s):
    if s is Link.empty:
        return s
    else:
        return Link(f(s.fir), map_link(f, s.res))

def filter_link(f, s):
    if s is Link.empty:
        return s
    else:
        filtered = filter_link(f, s.res)
        if f(s.fir):
            return Link(s.fir, filtered)
        else:
            return filtered

def is_empty(s):
        return s is Link.empty



s = Link(2, Link(3, Link(4)))
t = Link(345)
print(len(t))
print(t[1])
print(str(s))
print(s.__repr__())
print(s + t)
print(map_link(lambda x:x*x, s + t))
print(filter_link(lambda x:x % 2 == 0, s+t))


#############################################################
#使用上述数据结构实现集合的运算

def set_contains(s, v):
    """Return True if and only if set s contains v."""
    if is_empty(s):
        return False
    elif s.fir == v:
        return True
    else:
        return set_contains(s.res, v)

def push(s, v):
    if set_contains(s, v):
        return s
    else:
        return Link(v, s)

def intersect_set(set1, set2):
    """Return a set containing all elements common to set1 and set2."""
    return filter_link(lambda v: set_contains(set2, v), set1)

def union_set(set1, set2):
    """Return a set containing all elements either in set1 or set2."""
    set1_not_set2 = filter_link(lambda v: not set_contains(set2, v), set1)
    return set1_not_set2 + set2

#本函数的使用前提是：顺序存储
def intersect_set(set1, set2):
    if is_empty(set1) or is_empty(set2):
        return Link.empty
    else:
        e1, e2 = set1.fir, set2.fir
        if e1 == e2:
            return Link(e1, intersect_set(set1.res, set2.res))
        elif e1 < e2:
            return intersect_set(set1.res, set2)
        elif e2 < e1:
            return intersect_set(set1, set2.res)

s = Link(4, Link(1, Link(5)))
print(set_contains(s, 55))
print(push(s, 56))
print(s)
a = Link(4, Link(1, Link(5)))
b = Link(4, Link(3, Link(5)))
print(intersect_set(a, b))
print(union_set(a, b))
a = Link(4, Link(5, Link(6)))
b = Link(1, Link(2, Link(4)))
print(intersect_set(a, b))



####################################################################
##使用二叉搜索树来实现集合的运算

class Tree():
    def __init__(self, entry, left=None, right=None):
        self.entry = entry
        self.left = left
        self.right = right
    #Bug need fixed
    def __str__(self):
        if self == None:
            return "b"
        else:
            mid = str(self.entry)
            left = self.left.__str__()
            right = self.right.__str__()
            return str([left, mid, right])

def set_contains2(s, v):
    if s is None:
        return False
    elif s.entry == v:
        return True
    elif s.entry < v:
        return set_contains2(s.right, v)
    elif s.entry > v:
        return set_contains2(s.left, v)

def adjoin_set(s, v):
        if s is None:
            return Tree(v)
        elif s.entry == v:
            return s
        elif s.entry < v:
            return Tree(s.entry, s.left, adjoin_set(s.right, v))
        elif s.entry > v:
            return Tree(s.entry, adjoin_set(s.left, v), s.right)



print(adjoin_set(adjoin_set(adjoin_set(None, 2), 3), 1))



#####################################################################
#类的其他泛化的方法
class AC():

    def __init__(self, a):
        self.left = a
    def __bool__(self):
        return self.left != 0

#利用__call__函数生成可以调用的类
class Adder():
    def __init__(self,n):
        self.n = n
    def __call__(self, k):
        return self.n + k

f = Adder(3)
print(f(4))