"""
Ransom Note

Given two strings ransomNote and magazine, 

return true if ransomNote can be constructed by using the letters from magazine 

and false otherwise.

Each letter in magazine can only be used once in ransomNote.
"""

# Two hash maps 
# O(m)

def canConstruct(ransomNote, magazine):

	# check for obvious fail case 
	if len(ransomNote) > len(magazine):
		return False 

	# in Python, use the Counter class.
	magazine_counts = collections.Counter(magazine)
	ransom_note_counts = collections.Counter(ransomNote)

	# for each unique char in the ransom note:
	for char, count in ransom_note_counts.items():

		# check that the count of char in the magazine is equal 
		# or higher than the count in the ransom note 
		magazine_count = magazine_counts[char]

		if magazine_count < count:
			return False 

	# if we got this far, we can succesfully build the note 
	return True 
