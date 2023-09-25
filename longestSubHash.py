"""
Example 1: You are given a string s and an integer k. 

Find the length of the longest substring that contains at most k distinct characters.

For example, given s = "eceba" and k = 2, return 3. 

The longest substring with at most 2 distinct characters is "ece".
"""



def find_longest_substring(s, k):


	# Create a hash mp counts to keep count of the chars in the window 
	# Map letters to their frequency 
	# Length of counts is the number of distinct chars 
	counts = defaultdict(int)

	left = ans = 0 

	for right in range(len(s)):
		counts[s[right]] += 1 

		# decrements the leftmost char's counts by one 
		while len(counts) > k :
			counts[s[left]] -= 1 

			# if after deleting the count, the frequency of this char is 0
			# this char no longer belongs to the window
			# delete this char-counts pair 
			if counts[s[left]] == 0:
				del counts[s[left]] 

			# move the window to the right
			left += 1 

		ans = max(ans, right - left + 1)

	return ans 




