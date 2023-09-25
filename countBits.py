"""
Counting Bits
Given an integer n, return an array ans of length n + 1 
such that for each i (0 <= i <= n), 
ans[i] is the number of 1's in the binary representation of i.
"""

# O(n)
def countBits(n):
	ans = [0]*(n+1)
	for x in range(1, n+1):
	# x // 2 is x >> 1 and x % 2 is x & 1 
		ans[x] = ans[x >> 1] + (x & 1)
	return ans  

