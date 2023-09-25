"""
Make The String Great

Given a string s of lower and upper case English letters.

A good string is a string which doesn't have two adjacent characters s[i] and s[i + 1] where:

0 <= i <= s.length - 2

s[i] is a lower-case letter 

and s[i + 1] is the same letter 

but in upper-case or vice-versa.


To make the string good, 

you can choose two adjacent characters that make the string bad 

and remove them. 


You can keep doing this until the string becomes good.

Return the string after making it good. 

The answer is guaranteed to be unique under the given constraints.

Notice that an empty string is also good.

Input: s = "leEeetcode"
Output: "leetcode"

Explanation: In the first step, either you choose i = 1 or i = 2, 

both will result "leEeetcode" to be reduced to "leetcode".

Input: s = "abBAcC"
Output: ""
Explanation: We have many possible scenarios, and all lead to the same answer. For example:
"abBAcC" --> "aAcC" --> "cC" --> ""
"abBAcC" --> "abBA" --> "aA" --> ""

"""
"""
One thing to note is that to judge if two adjacent characters make a pair? 

We do easily tell that patterns like aA, Bb, cC are pairs, but how to implement the code? 

We can use the their ASCII values as reference, each character has a unique ASCII value:

a = 97, A = 65
b = 98, B = 66
c = 99, C = 67
...
z = 122, Z = 90

Thus we can tell that two characters make a pair, 

when and only when their ASCII values differ by 32 

(Since the sentence only contains letters of alphabet, 

we do not need to consider about other speical characters). 
"""

# stack O(n)

def makeGood(s):

	# use stack to store the visited chars 
	stack = []

	# iterate over 's'
	for curr_char in list(s):

		# if the cur char make a pair with the last char in the stack 
		# remove both of them
		# otherwise, add the cur char to stack
		if stack and abs(ord(curr_char) - ord(stack[-1])) == 32:
			stack.pop()

		else:
			stack.append(curr_char)

	# return the string concatenated by all chars left in the stck 
	return "".join(stack)




























