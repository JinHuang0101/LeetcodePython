"""
Example 2: You are given a binary string s 
(a string containing only "0" and "1"). 

You may choose up to one "0" and flip it to a "1". 

What is the length of the longest substring achievable that contains only "1"?

Constraint: You can only have at most one "0" in the window 


For example, given s = "1101100111", the answer is 5. 
If you perform the flip at index 2, the string becomes 1111100111.
"""


# sliding window 

def lenLongest1(s):

	# curr is the current number of zeors in the window 
	left = curr = ans = 0  

	# Constraint: no more than one 0, curr cannot be greater than 1
	for right in range(len(s)):

		# expand window by adding right element, 
		# if window right adds a 0, 
		if s[right] == "0":
			curr += 1 

		# need to check the constraint and decide if to drop leftmost 
		while curr > 1:

			# have to drop left zero 
			if s[left] == "0":
				curr -= 1 

			left += 1 

		ans = max(ans, right - left + 1) # keep track of each valid window length 

	return ans 

