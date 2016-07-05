#实现可以改变的链表
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


def mutble_link():
    contents = empty
    def dispatch(message, value=None):
        nonlocal contents
        if message == 'len':
            return len_list(contents)
        elif message == 'push_first':
            contents =  make_list(value, contents)
            return contents
        elif message == 'pop_first':
            first = contents[0]
            contents = contents[1]
            return first
        elif message == 'get_item':
            return get_item(contents, value)
        elif message == 'str':
            return contents
    return dispatch        
def transfer(li):
    s = mutble_link()
    for e in li:
        s('push_first',e)
    return s


li = [1, 2, 3, 4]
newlist = transfer(li)
print(newlist('str'))
print(newlist('pop_first'))
print(newlist('str'))


#################################################
#实现字典
def dictionary():
    contents=[]
    def get_item(key):
        nonlocal contents
        mathes = [r for r in contents if r[0] == key]
        if(len(mathes) == 0):
            return None
        else:
            return mathes[0][1]
    def set_item(key, value):
        nonlocal contents
        no_mathes = [r for r in contents if r[0]!= key]
        contents = no_mathes + [[key, value]]
    def str():
        nonlocal contents
        return contents
    def dispatch(message, key=None,value=None):
        nonlocal contents
        if message == 'get':
            return get_item(key)
        elif message == 'set':
            return set_item(key, value)
        elif message == 'str':
            return str()
    return dispatch


dic = dictionary()
dic('set','zhanglanqing', 20)
print(dic('str'))

##############################################################

#账户的字典实现
def account(initial_balance):
    def deposit(amount):
        dispatch['balance'] += amount
        return dispatch['balance']
    def withdraw(amount):
        if amount > dispatch['balance']:
            return 'Insufficient funds'
        dispatch['balance'] -= amount
        return dispatch['balance']
    dispatch = {'deposit':   deposit,
                'withdraw':  withdraw,
                'balance':   initial_balance}
    return dispatch

def withdraw(account, amount):
    return account['withdraw'](amount)
def deposit(account, amount):
    return account['deposit'](amount)
def check_balance(account):
    return account['balance']


a = account(20)
deposit(a, 5)
withdraw(a, 17)
check_balance(a)
#####################################################