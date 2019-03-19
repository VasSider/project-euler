class NumbWord:
	__word = ["one","two","three","four","five","six","seven","eight","nine","ten","eleven","twelve","thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety", "hundred", "thousand"]
	__dec = [30,40,50,60,70,80,90,100]
      
	def ConvertToWord(self, number):
		if number <1:
			return 'Error: Numbers must be greater than zero'
		elif number <= 20:
			return NumbWord.__word[number-1]
		elif number <100:
			for i in range (0,len(NumbWord.__dec)+1):
				if number <NumbWord. __dec[i]:
					if number % 10==0:
						return NumbWord.__word[19+i] 
					else:
						return NumbWord.__word[19+i] + NumbWord.ConvertToWord(NumbWord, number - NumbWord.__dec[i] + 10)
					break
		elif number < 1000:
			if number % 100 ==0:
				return NumbWord.__word[number//100-1]+NumbWord.__word[27]
			else:
				return NumbWord.__word[number//100-1]+NumbWord.__word[27]+ 'and' +  NumbWord.ConvertToWord(NumbWord, number % 100)
		elif number == 1000:
			return NumbWord.__word[0]+NumbWord.__word[28]
		else:
			return 'Error: Number out of range.'
	
	def CountLetterNumb(self,low,upper):
		res = 0
		str = ''
		while low<= upper:		
			str = NumbWord.ConvertToWord(NumbWord, low)
			res += len(str)
			low +=1
			if str.find('Error:') > -1:
				res = 'Error: Number out of range'
				break
			
		return res
			
		
		

if __name__=='__main__':
				
	x=NumbWord()
	print(x.ConvertToWord(899)) # for ex. spell 899
	print(x.CountLetterNumb(1,1000))

     
         
  	
  	
  	