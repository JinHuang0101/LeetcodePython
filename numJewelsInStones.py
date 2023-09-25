"""
Jewels and Stones

You're given strings jewels representing the types of stones that are jewels, 

and stones representing the stones you have. 

Each character in stones is a type of stone you have. 

You want to know how many of the stones you have are also jewels.

Letters are case sensitive, so "a" is considered a different type of stone from "A".

Example 1:

Input: jewels = "aA", stones = "aAAbbbb"
Output: 3

"""

# hash set 

# For each stone, check whether it matches any of the jewels. 
# O(J.length + S.length)
def numJewelsInStones(J, S):
	Jset = set(J)

	return sum(s in Jset for s in S)

