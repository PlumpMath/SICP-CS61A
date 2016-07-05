#本文件着重解决复杂度问题

def fib(n):
    if n == 1:
        return 0
    if n == 2:
        return 1
    return fib(n-2) + fib(n-1)


#################################################
#利用闭包的特征和装饰器的语法糖，检测函数调用的次数等等
def count(f):
    def counted(*args):
        counted.call_count += 1
        return f(*args)
    counted.call_count = 0
    return counted

#TODO:语法不太明白
def count_frames(f):
        def counted(*args):
            counted.open_count += 1
            counted.max_count = max(counted.max_count, counted.open_count)
            result = f(*args)
            counted.open_count -= 1
            return result
        counted.open_count = 0
        counted.max_count = 0
        return counted

fib = count(fib)
print(fib(3))
print(fib.call_count)

################################################
###实现记忆化搜索
def memo(f):
    cache = {}
    def memoized(n):
        if n not in cache:
            cache[n] = f(n)
        return cache[n]
    return memoized

fib = memo(fib)

print(fib(200))

