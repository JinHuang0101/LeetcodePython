"""
Maximum Number of Balloons

Given a string text, 

you want to use the characters of text 

to form as many instances of the word 

"balloon" as possible.


You can use each character in text at most once. 

Return the maximum number of instances that can be formed.
"""

# the potential of a char: the number of times that "ballon" can be produced
# assuming there is an infinite supply of other chars
# e.g., if b has a quantity of x, then x balloon 
# l, x, then x/2 ballon

def maxNumberOfBallons(text):
	bCount = 0
	aCount = 0 
	lCount = 0 
	oCount = 0 
	nCount = 0 

	# count the frequency of all five chars 
	for i in range(len(text)):
		if text[i] == 'b':
			bCount += 1 
		elif text[i] == 'a':
			aCount += 1 
		elif text[i] == 'l':
			lCount += 1
		elif text[i] == 'o':
			oCount += 1 
		elif text[i] == 'o':
			oCount += 1 
		elif text[i] == 'n':
			nCount += 1 

	# find the potential of each char 
	# except for 'l' and'o' the potential is equal to the frequency 
	lCount = lCount / 2 
	oCount = oCount / 2 

	# find the bottleneck
	return min(bCount, aCount, lCount, oCount, nCount)
	
