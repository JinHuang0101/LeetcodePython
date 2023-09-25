"""
Example 3: 1941. Check if All Characters Have Equal Number of Occurrences

Given a string s, determine if all characters have the same frequency.

For example, given s = "abacbc", return true. 

All characters appear twice. 

Given s = "aaabb", return false. "a" appears 3 times, "b" appears 2 times. 3 != 2.
"""

def occurEqual(s):

	# use a hash map counts to count all char frequencies 
	counts = defaultdict(int)

	# iterate through s and get the frequency of every char 
	for c in s:
		counts[c] += 1 

	frequencies = counts.values()

	# check if all frequencies are the same
	# by putting all frequencies in a set
	# and check if the length is 1 
	return len(set(frequencies)) == 1 


