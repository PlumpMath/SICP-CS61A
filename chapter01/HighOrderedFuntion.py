
def improve(update, close, guess=1):
        while not close(guess):
            guess = update(guess)
        return guess

def approx_eq(x, y, tolerance=1e-15):
        return abs(x - y) < tolerance

#################################################
#solving x * x = a  
def sqrt(a):

    def sqrt_update(x):
        return average(x, a/x)

    def sqrt_close(x):
        return approx_eq(x * x, a)
    return improve(sqrt_update, sqrt_close)


def average(x, y):
        return (x + y)/2

print(sqrt(16))

########################################
#we can ignore the global
a = 3
def test():
    #global a
    return a+2
print(test())

#######################################
#given fx and f'(x) find the solution of f(x) = 0
def newton_update(f, df):
        def update(x):
            return x - f(x) / df(x)
        return update

def find_zero(f, df):
        def near_zero(x):
            return approx_eq(f(x), 0)
        return improve(newton_update(f, df), near_zero)

def square_root_newton(a):

        def f(x):
            return x * x - a

        def df(x):
            return 2 * x
        
        return find_zero(f, df)

#############################################################
#find the solution of x**n = a 
def n_square_root_newton(n,a):

	def fx(x):
		return pow(x,n)-a

	def df(x):
		return n*pow(x,n-1)

	return find_zero(fx,df)


print(n_square_root_newton(2,256))

##############################################################
#two ways to compose functions
def curry2(f):
        """Return a curried version of the given two-argument function."""
        def g(x):
            def h(y):
                return f(x, y)
            return h
        return g

def uncurry2(g):
        """Return a two-argument version of the given curried function."""
        def f(x, y):
            return g(x)(y)
        return f

after_wraped = curry2(pow)
print(after_wraped(2)(3))


##########################################################
#Haskell-style
def multifunction(a,b,c,d):
	return a+b+c+d

def wrap(a):
	def g(b):
		def h(c):
			def i(d):
				return multifunction(a,b,c,d)
			return i
		return h
	return g

print(wrap(1)(2)(3)(4))

###########################################################
#lambda functions 
def compose1(f, g):
        return lambda x: f(g(x))
compose1 = lambda f,g: lambda x: f(g(x))

############################################################
#decorater
def trace(fn):
        def wrapped(x):
            print('-> ', fn, '(', x, ')')
            return fn(x)
        return wrapped

@trace
def triple(x):
    return 3 * x

print(triple(4))

#############################################################
#Tail Recursion and Repetition
def fib2(fk1, fk, k, n):
	"""Assuming FK1 and FK2 are fib(K-1) and fib(K)
	in the Fibonacci sequence and that N>=K, return fib(N)."""
	if n == k:
		return fk
	else:
		return fib2(fk,fk1+fk,k+1,n)

def fib(n):
	if n <= 1:
		return n
	else:
		return fib2(0, 1, 1, n)

print(fib(4))

###############################################
#newton-method-iterator-sovling
def iter_solve(guess, done, update, iteration_limit=130):
	"""Return the result of repeatedly applying UPDATE,
	starting at GUESS, until DONE yields a true value
	when applied to the result. Causes error if more than
	ITERATION_LIMIT applications of UPDATE are necessary."""
	while not done(guess):
		if iteration_limit <= 0:
			raise ValueError("failed to converge")
		guess, iteration_limit = update(guess), iteration_limit-1
	return guess


def newton_solve(func, deriv, start, tolerance):
	"""Return x such that |FUNC(x)| < TOLERANCE, given initial
	estimate START and assuming DERIV is the derivatative of FUNC."""
	def close_enough(x):
		return abs(func(x)) < tolerance
	def newton_update(x):
		return x - func(x) / deriv(x)

	return iter_solve(start, close_enough, newton_update)

print(newton_solve(lambda x: x*x - 4, lambda x: 2 * x, 1, 1e-15))


def logarithm(a, base = 2):
	return newton_solve(lambda x: base**x - a, lambda x: x * base**(x-1), 1, 1e-5)

print(logarithm(4))

#################################################################
#How-to-find f'(x)
def approx_deriv(func, delta = 1e-5):
	return lambda x: (func(x + delta) - func(x)) / delta

dx=approx_deriv(lambda x: x ** 3)
print(dx(2))

#############to sove any equalization with this method###########

def sovle_equalization(func,start=1,tolerance=1e-10):
	def approx_deriv(f, delta = 1e-5):
		return lambda x: (f(x + delta) - f(x)) / delta
	return newton_solve(func, approx_deriv(func), start, tolerance)

print(sovle_equalization(lambda x: x * x * x + x * x + x - 1))




##################################################################
######Using Generalized iter solve2 for the Secant Method#########
#########################there is no dx###########################

def iter_solve2(guess, done, update, state=None):
	"""Return the result of repeatedly applying UPDATE,
	starting at GUESS and STATE, until DONE yields a true value
	when applied to the result. Besides a guess, UPDATE
	also takes and returns a state value, which is also passed to
	DONE."""
	while not done(guess, state):
		guess, state = update(guess, state)
	return guess

def secant_solve(func, start0, start1, tolerance):

	def close_enough(x, state):
		return abs(func(x)) < tolerance

	def secant_update(xk, xk1):
		return (xk - func(xk) * (xk - xk1))/ (func(xk) - func(xk1),xk)

	return iter_solve2(start1, close_enough, secant_update, start0)

###################################################################