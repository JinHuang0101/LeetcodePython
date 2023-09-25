"""
Example 1: 49. Group Anagrams

Given an array of strings strs, group the anagrams together.

For example, given strs = ["eat","tea","tan","ate","nat","bat"], 

return [["bat"],["nat","tan"],["ate","eat","tea"]].

"""

# Intuition 1: Use two hash maps 
# count all chars in each string 
# compare if the hash maps are the same 

# Intuition 2: checking if they are equal after both being sorted.
# All strings in a group will be the same when sorted
# so use the sorted version as a key 
# map these keys to the groups themselves in a hash map 
# our answer is the values of the hash map 
# each group has its own identifier (the sorted string),
# then we use this identifier to group them in a hash map 

from collections import defaultdict

def groupAnagrams(strs):

	# use the sorted strings as a key
	groups = defaultdict(list)

	# identifier: sorted version of a string as a key
	# map the sorted version to itself
	for s in strs:
		key = "".join(sorted(s))
		groups[key].append(s)

	return groups.values()
	

