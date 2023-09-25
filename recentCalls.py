"""
Example: 933. Number of Recent Calls

Implement the RecentCounter class. 

It should support ping(int t), 

which records a call at time t, 

and then returns an integer 

representing the number of calls that have happened in the range [t - 3000, t]. 

Calls to ping will have increasing t.
"""

from collections import deque 

class RecentCounter:
	def __init__(self):
		self.queue = deque()

	def ping(t):

		while self.queue and self.queue(0) < t - 3000:
			self.queue.popleft()

		self.queue.append(t)

		return len(self.queue)

# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)



