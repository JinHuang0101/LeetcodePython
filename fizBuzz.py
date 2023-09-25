"""
Fizz Buzz
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.
Input: n = 3
Output: ["1","2","Fizz"]
"""

# O(N)
def fizBuzz(n):

	# return an answer list
	ans = []

	# the array (1 - indexed), starting from 1
	for num in range(1, n+1):
		div_by_3 = (num % 3 == 0)
		div_by_5 = (num % 5 == 0)

		if div_by_3 and div_by_5:

			# div by both 3 and 5, FizzBuzz 
			ans.append("FizzBuzz")

		elif div_by_3:

			# div by 3, add Fizz 
			ans.append("Fizz")

		elif div_by_5:

			# div by 5, add Buzz 
			ans.append("Buzz")
		else:
			# other 
			ans.append(str(num))

	return ans  

