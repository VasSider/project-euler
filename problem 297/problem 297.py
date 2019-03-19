import time

class Memoize(object):
    def __init__(self, func):
        self.func = func
        self.cache = {}
    def __call__(self, *args):
        if args in self.cache:
            return self.cache[args]
        ret = self.func(*args)
        self.cache[args] = ret
        return ret
        
@Memoize        
def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)

@Memoize
def SubFibDig(n):
	if n<=3:
		return n
	else:
		return SubFibDig(n-1) + SubFibDig(n-2) + fib(n-2) - 1
		
@Memoize
def Z(n):
	i=1
	while fib(i)<=n:
		i+=1
	if fib(i-1)==n:
		return SubFibDig(i-1)
	else:
		diff=n-fib(i-1)
		return SubFibDig(i-1) + diff + Z(diff)

if __name__=='__main__':
	start=time.time()
	print(Z(10**17))
	print(time.time()-start)
	
		
 	