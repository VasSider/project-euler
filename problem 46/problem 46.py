import numpy as np;
import time 
def SieveOfEratosthenes(n): 
    prime = [True for i in range(n+1)] 
    p = 2
    while (p * p <= n): 
        if (prime[p] == True): 
            for i in range(p * p, n+1, p): 
                prime[i] = False
        p += 1
    ls=[]
    for p in range(2, n): 
        if prime[p]: 
            ls.append(p)
    return ls

if __name__=='__main__': 
    n = 100000
    primes= np.array(SieveOfEratosthenes(n))
    double_squared= np.array(list(map(lambda x: 2*x**2, range(int(n/4)))))
  
    start=time.time()  
    for i in range(17,n,2):
        j = int(np.amax(np.where(primes<=i)))
        k = int(np.amax(np.where(double_squared<i)))
        equal = any(i-x in double_squared[:k+1] for x in primes[:j+1])
        if equal==False:
            print (i)
            break
    print (time.time()-start)



