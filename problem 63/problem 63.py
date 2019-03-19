import math

#def DigCount(n):
#	n_tenth=n//10
#	if n_tenth==0:
#		return 1
#	else:
#		return DigCount(n_tenth) +1
#
# if you don' t trust log10 method to find the 
#amount of digits you can use DigCount function

if __name__=='__main__':
	count=0
	for i in range(1,10):
		pow=1
		while int(math.log10(i**pow))+1 >= pow:
			if  int(math.log10(i**pow))+1== pow:
				count+=1
			pow+=1
			
	print(count)	