"""
Given a string array words, return an array of 
all characters that show up in all strings within the words (including duplicates). 

You may return the answer in any order.

------------------------
string array words: an array  of strings that are words
words = ["bella","label","roller"]

Output: ["e","l","l"]
"""

def commonChars(words):

	charArray = []

	for i in words[0]:
		t = True 
		for j in range(len(words)):
			if i not in words[j]:
				t = False 
			else:
				cur = list(words[j])
				cur.pop(cur.index(i))
				words[j] = ''.join(cur) 

		if t: 
			charArray.append(i) 
		
	return charArray 
