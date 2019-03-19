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
	start=time.time()
	n = 2*10**6
	print(sum(SieveOfEratosthenes(n)))
	print(time.time()-start)

    			
    	
    	
    	
    