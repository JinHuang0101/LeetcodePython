"""
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

example: 2 is written as II, 12 is written as XII, 27 is written as XXVII,
Roman numerals are usually written largest to smallest from left to right. 
Instead, the number four is written as IV.
The same principle applies to the number nine, which is written as IX.

I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
"""

# O(1)
values = {
	"I" : 1,
	....
}

def romanToInt(s):
	total = 0 
	i = 0 
	while i < len(s):
		# if this is the subtractive case 
		if i + 1 < len(s) and values[s[i]] < values[s[i+1]]: 
			total += values[s[i+1]] - values[s[i]]
			i += 2 

		# If not the subractive case 
		else:
			total += values[s[i]]
			i += 1 
	return total 




