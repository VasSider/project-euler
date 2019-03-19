new_val=0
prev=2
pre_prev=1
sum=2

while new_val<=4e6:
	new_val=prev+pre_prev
	
	if new_val%2==0:
		sum+=new_val
	
	pre_prev=prev
	prev=new_val

print(sum)
