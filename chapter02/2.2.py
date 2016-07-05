#implement pair without list,just functional programming
def pair(x, y):
    def get(index):
        if index == 1:
            return x
        elif index == 2:
            return y
        else:
            raise ValueError()
    return get

def select(x,index):
    return x(index)

    
tar = pair(1, 2)
print(select(tar,2))
print('zhanglanqing' * 2)
print('zhang' in 'zhanglanqing')