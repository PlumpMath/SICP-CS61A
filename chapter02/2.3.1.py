#实现树
def make_tree(root, branches=[]):
    for branch in branches:
        assert is_tree(branch), 'branches must be a tree'
    return [root] + [branches]
def get_root(tree):
    return tree[0]
def get_branches(tree):
    return tree[1]
def is_tree(tree):
    if type(tree) != list or len(tree) < 1:
        return False
    for branch in get_branches(tree):
        if is_tree(branch) == False:
            return False
    return True
def is_leaf(tree):
    return not get_branches(tree)

def count_nodes(tree):
    if is_tree(tree) == False:
        return 0
    if get_branches(tree) == []:
        return 1
    sum = 1
    for branch in get_branches(tree):
        sum += count_nodes(branch)
    return sum

def count_leaves(tree):
    if is_tree(tree) == False:
        return 0
    if get_branches(tree)==[]:
        return 1
    else:
        sum = 0
        for branch in get_branches(tree):
            sum += count_leaves(branch)
        return sum

def fib_tree(n):
    if n == 0 or n == 1:
        return make_tree(n)
    else:
        left = fib_tree(n-1)
        right = fib_tree(n-2)
        root = get_root(left) + get_root(right)
        return make_tree(root, [left, right])


#树的应用建立划分树
def partition_tree(n, m):
    """Return a partition tree of n using parts of up to m."""
    if n == 0:
        return make_tree(True)
    elif n < 0 or m == 0:
        return make_tree(False)
    else:
        left = partition_tree(n-m, m)
        right = partition_tree(n, m-1)
        return make_tree(m, [left, right])

#打印划分树，每一条从根节点到叶子的路径都组成一条加法公式
def print_parts(tree, partition=[]):
    if is_leaf(tree):
        if get_root(tree):
            print(' + '.join(partition))
    else:
        left, right = get_branches(tree)
        m = str(get_root(tree))
        print_parts(left, partition + [m])
        print_parts(right, partition)


p = partition_tree(3,2)
print_parts(p)


#实现链表
empty = 'NULL'
def make_list(first, second=empty):
    assert is_list(second), 'second element must be list'
    return [first, second]

def is_list(linklist):
    return linklist == empty or len(linklist) == 2 and is_list(linklist[1])

def len_list(linklist):
    if linklist == empty:
        return 0
    else:
        return len_list(linklist[1]) + 1
def get_item_recur(linklist, index):
    if linklist == empty:
        return -1
    elif index == 1:
        return linklist[0]
    else:
        return get_item_recur(linklist[1], index-1)
def get_item_iter(linklist, index):
    k = 0
    while k < index-1:
        linklist = linklist[1]
        if linklist == empty:
            return -1
        k += 1
    return linklist[0]

def extend_link(s, t):
    if s == empty:
        return t
    else:
        return make_list(s[0], extend_link(s[1], t))

def apply_to_all_link(f, linklist):
    if linklist == empty:
        return linklist
    else:
        return make_list(f(linklist[0]), apply_to_all_link(f,linklist[1]))

def keep_if_link(f, s):

    if s == empty:
        return s
    else:
        kept = keep_if_link(f, s[1])
        if f(s[0]) == True:
            return make_list(s[0], kept)
        else:
            return kept
def join_link(s, separator):
    if s == empty:
        return ""
    elif s[1] == empty:
        return str(s[0])
    else:
        return str(s[0]) + separator + join_link(s[1], separator)


l = make_list(1, make_list(2, make_list(3, make_list(4))))
m = make_list(1, make_list(2, make_list(3)))
print(get_item_iter(l,1))
print(l)
print(m)
print(extend_link(m, l))
print(apply_to_all_link(lambda x: x*100, l))

###############################################################


