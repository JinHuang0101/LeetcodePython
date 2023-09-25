"""
A pangram is a sentence where every letter of the English alphabet appears at least once.

Given a string sentence containing only lowercase English letters, 

return true if sentence is a pangram, or false otherwise.

Input: sentence = "thequickbrownfoxjumpsoverthelazydog"
Output: true
Explanation: sentence contains at least one of every letter of the English alphabet.

"""

# hash, use set, count length of set

def checkIfPangram(sentence):


	# add every letter of sentence to hash set "seen"
	seen = set(sentence)

	# check the size 
	return len(seen) == 26 

