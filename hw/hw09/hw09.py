## DATA STRUCTURES ##

# Linked List Class
class Link:
    """
    >>> s = Link(1, Link(2, Link(3)))
    >>> s
    Link(1, Link(2, Link(3)))
    >>> len(s)
    3
    >>> s[2]
    3
    >>> s = Link.empty
    >>> len(s)
    0
    """
    empty = ()

    def __init__(self, first, rest=empty):
        assert rest is Link.empty or isinstance(rest, Link)
        self.first = first
        self.rest = rest

    def __repr__(self):
        if self.rest is not Link.empty:
            rest_str = ', ' + repr(self.rest)
        else:
            rest_str = ''
        return 'Link({0}{1})'.format(repr(self.first), rest_str)

    def __len__(self):
        """ Return the number of items in the linked list.

        >>> s = Link(1, Link(2, Link(3)))
        >>> len(s)
        3
        >>> s = Link.empty
        >>> len(s)
        0
        """
        return 1 + len(self.rest)

    def __getitem__(self, i):
        """Returning the element found at index i.

        >>> s = Link(1, Link(2, Link(3)))
        >>> s[1]
        2
        >>> s[2]
        3
        """
        if i == 0:
            return self.first
        else:
            return self.rest[i-1]

    def get_ith_link(self, n):
        i = 0
        ret = self
        while i < n:
            ret = ret.rest
            i += 1
        return ret



class Tree:
    def __init__(self, label, children=()):
        self.label = label
        for branch in children:
            assert isinstance(branch, Tree)
        self.children = list(children)

    def __repr__(self):
        if self.children:
            children_str = ', ' + repr(self.children)
        else:
            children_str = ''
        return 'Tree({0}{1})'.format(self.label, children_str)

    def is_leaf(self):
        return not self.children


## QUESTIONS ##

# Q1

def nearest_two(x):
    """Return the power of two that is nearest to x.

    >>> nearest_two(8)    # 2 * 2 * 2 is 8
    8.0
    >>> nearest_two(11.5) # 11.5 is closer to 8 than 16
    8.0
    >>> nearest_two(14)   # 14 is closer to 16 than 8
    16.0
    >>> nearest_two(2015)
    2048.0
    >>> nearest_two(.1)
    0.125
    >>> nearest_two(0.75) # Tie between 1/2 and 1
    1.0
    >>> nearest_two(1.5)  # Tie between 1 and 2
    2.0

    """
    if x == 1:
        return 1.0
    elif x > 1:
        i = 1
        while 2**i < x:
            i = i + 1
        if abs(2**i - x) <= abs(2**(i-1) - x):
            return 2**i*1.0
        else:
            return 2**(i-1)*1.0
    else:
        i = -1
        while 2**i > x:
            i = i - 1
        if abs(2**i - x) < abs(2**(i+1) - x):
            return 2**i*1.0
        else:
            return 2**(i+1)*1.0


# Q2

def repeated(f, n):
    """Returns a single-argument function that takes a value, x, and applies
    the single-argument function F to x N times.
    >>> repeated(lambda x: x*x, 3)(2)
    256
    """
    def h(x):
        for k in range(n):
            x = f(x)
        return x
    return h




def smooth(f, dx):
    """Returns the smoothed version of f, g where

    g(x) = (f(x - dx) + f(x) + f(x + dx)) / 3

    >>> square = lambda x: x ** 2
    >>> round(smooth(square, 1)(0), 3)
    0.667
    """
    return lambda x: (f(x) + f(x-dx) + f(x+dx)) / 3


def n_fold_smooth(f, dx, n):
    """Returns the n-fold smoothed version of f
    # 我觉的这道题目有问题啊，他让用lambda根本就是误导好吗？，这里根本就是迭代啊
    >>> square = lambda x: x ** 2
    >>> round(n_fold_smooth(square, 1, 3)(0), 3)
    2.0
    """
    ret = smooth(f, dx)
    i = 1
    while i < n:
        ret = smooth(ret, dx)
        i = i + 1
    return ret



# Q3

def near_golden(perimeter):
    """Return the integer height of a near-golden rectangle with PERIMETER.

    >>> near_golden(42) # 8 x 13 rectangle has perimeter 42
    8
    >>> near_golden(68) # 13 x 21 rectangle has perimeter 68
    13
    >>> result = near_golden(100) # return, don't print
    >>> result
    19

    """
    n = perimeter // 2
    i = 1
    recminer = -1
    minabs = 100000
    while i < n // 2:
        miner = i
        maxer = n - i
        if abs(maxer/miner - 1 - miner/maxer) < minabs:
            recminer = miner
            minabs = abs(maxer/miner - 1 - miner/maxer)
        i = i + 1
    return recminer


# Q4

def is_circular(G):
    """Return true iff G represents a circular directed graph."""
    for v in G:
        if reaches_circularity(G, v):
            return True
    return False
def reaches_circularity(G, v0):
    """Returns true if there is a circularity in G in some path
    starting from vertex V0.
    >>> G = { 'A': ['B', 'D'], 'B': ['C'], 'C': ['F'], 'D': ['E'], 
    ...       'E': ['F'], 'F': ['G'], 'G': ['A'] }
    >>> is_circular(G)
    True
    >>> G['F'] = []
    >>> is_circular(G)
    False
    """
    size = len(G)
    # 采用了一种比较低效的方式，就是检测一个节点是不是在环上，其实这里也可以采用迭代的方式
    def is_path_to_cycle(v1, num):
        if num == size:
            return False
        for w in G[v1]:
            if v0 == w:
                return True
            if is_path_to_cycle(w, num + 1):
                return True
        return False
    return is_path_to_cycle(v0, 0)



# Q5



def intersection(xs, ys):
    """
    >>> a = Link(1)
    >>> intersection(a, Link.empty) is Link.empty
    True

    >>> b = a
    >>> intersection(a, b).first # intersection begins at a
    1

    >>> looks_like_a = Link(1)
    >>> intersection(a, looks_like_a) is Link.empty # no intersection! (identity vs value)
    True

    >>> b = Link(1, Link(2, Link(3, a)))
    >>> a.first = 5
    >>> intersection(a, b).first # intersection begins at a
    5

    >>> c = Link(3, b)
    >>> intersection(b, c).first # intersection begins at b
    1
    >>> intersection(c, b).first # intersection begins at b
    1

    >>> intersection(a, c).first # intersection begins at a
    5
    """
    x_len = len(xs)
    y_len = len(ys)
    if x_len == y_len:
        pass
    elif x_len > y_len:
        for _ in range(0, x_len - y_len):
            xs = xs.rest
    elif y_len > x_len:
        for _ in range(0, y_len - x_len):
            ys = ys.rest

    while True:
        if xs is ys:
            return xs
        xs = xs.rest
        ys = ys.rest


# Q6

def deck(suits, ranks):
    """Creates a deck of cards (a list of 2-element lists) with the given
    suits and ranks. Each element in the returned list should be of the form
    [suit, rank].

    >>> deck(['S', 'C'], [1, 2, 3])
    [['S', 1], ['S', 2], ['S', 3], ['C', 1], ['C', 2], ['C', 3]]
    >>> deck(['S', 'C'], [3, 2, 1])
    [['S', 3], ['S', 2], ['S', 1], ['C', 3], ['C', 2], ['C', 1]]
    >>> deck([], [3, 2, 1])
    []
    >>> deck(['S', 'C'], [])
    []
    """

    return [[x, y] for x in suits for y in ranks]


# Q7

def riffle(deck):
    """Produces a single, perfect riffle shuffle of DECK, consisting of
    DECK[0], DECK[M], DECK[1], DECK[M+1], ... where M is position of the
    second half of the deck.  Assume that len(DECK) is even.
    >>> riffle([3, 4, 5, 6])
    [3, 5, 4, 6]
    >>> riffle(range(20))
    [0, 10, 1, 11, 2, 12, 3, 13, 4, 14, 5, 15, 6, 16, 7, 17, 8, 18, 9, 19]
    """
    origin = list(deck)
    ret = []
    for i in range(len(origin)//2):
        ret.append(origin[i])
        ret.append(origin[i + len(origin)//2])
    return ret






# Q8

def make_advanced_counter_maker():
    """Makes a function that makes counters that understands the
    messages "count", "global-count", "reset", and "global-reset".
    See the examples below:

    >>> make_counter = make_advanced_counter_maker()
    >>> tom_counter = make_counter()
    >>> tom_counter('count')
    1
    >>> tom_counter('count')
    2
    >>> tom_counter('global-count')
    1
    >>> jon_counter = make_counter()
    >>> jon_counter('global-count')
    2
    >>> jon_counter('count')
    1
    >>> jon_counter('reset')
    >>> jon_counter('count')
    1
    >>> tom_counter('count')
    3
    >>> jon_counter('global-count')
    3python3 ok -q partial_tree
    >>> jon_counter('global-reset')
    >>> tom_counter('global-count')
    1
    """
    global_counter = 0
    def make_counter():

        cnt = 0
        def do_action(message):

            def f_add():
                nonlocal cnt
                cnt += 1
                return cnt
            def f_reset():
                nonlocal cnt
                cnt = 0
            if message == 'count':
                return f_add()
            elif message == 'reset':
                return f_reset()
            elif message == 'global-count':
                nonlocal global_counter
                global_counter += 1
                return global_counter
            elif message == 'global-reset':
                nonlocal global_counter
                global_counter = 0

        return do_action

    return make_counter





# Q9

def partial_tree(s, n):
    """Return a balanced tree of the first n elements of Link s, along with
    the rest of s.

    Examples of balanced trees:

    Tree(1)                      # leaf
    Tree(1, [Tree(2)])           # one branch is a leaf
    Tree(1, [Tree(2), Tree(3)])  # two branches with one node each

    Examples of unbalanced trees:

    Tree(1, [Tree(2, [Tree(3)])])            # one branch not a leaf
    Tree(1, [Tree(2),                        # Mismatch: branch with 1 node
             Tree(3, [Tree(4, [Tree(5)])])]) #        vs branch with 3 nodes

    >>> s = Link(1, Link(2, Link(3, Link(4, Link(5)))))
    >>> partial_tree(s, 3)
    (Tree(2, [Tree(1), Tree(3)]), Link(4, Link(5)))
    >>> t = Link(-2, Link(-1, Link(0, s)))
    >>> partial_tree(t, 7)[0]
    Tree(1, [Tree(-1, [Tree(-2), Tree(0)]), Tree(3, [Tree(2), Tree(4)])])
    >>> partial_tree(t, 7)[1]
    Link(5)
    """
    if n == 1:
        return (Tree(s.first), s.rest)
    elif n == 2:
        return (Tree(s.first, [Tree(s.rest.first)]), s.res3t.rest)
    else:
        left_size = (n-1)//2
        right_size = n - left_size - 1

        left_branch = partial_tree(s, left_size)[0]
        root = s[left_size]
        right_branch = partial_tree(s.get_ith_link(left_size + 1), right_size)[0]
        return (Tree(root, [left_branch, right_branch]), s.get_ith_link(n))


def sequence_to_tree(s):
    """Return a balanced tree containing the elements of sorted Link s.

    Note: this implementation is complete, but the definition of partial_tree
    above is not complete.

    >>> sequence_to_tree(Link(1, Link(2, Link(3))))
    Tree(2, [Tree(1), Tree(3)])
    >>> elements = Link(1, Link(2, Link(3, Link(4, Link(5, Link(6, Link(7)))))))
    >>> sequence_to_tree(elements)
    Tree(4, [Tree(2, [Tree(1), Tree(3)]), Tree(6, [Tree(5), Tree(7)])])
    """
    return partial_tree(s, len(s))[0]
