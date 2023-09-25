def dna_match_topdown_recursion(DNA1, DNA2, ind1, ind2, dp):
	if ind1 <0 or ind2 < 0:
		return 0

	if dp[ind1][ind2] != -1:
		return dp[ind1][ind2]

	if DNA1[ind1] == DNA2[ind2]:
		dp[ind1][ind2] = 1 + dna_match_topdown_recursion(DNA1, DNA2, ind1-1, ind2-1, dp)

	else:
		dp[ind1][ind2] = 0 + max(dna_match_topdown_recursion(DNA1, DNA2, ind1, ind2-1, dp), dna_match_topdown_recursion(DNA1, DNA2, ind1-1, ind2, dp))

	return dp[ind1][ind2]


def dna_match_topdown(DNA1, DNA2):
    n1 = len(DNA1)
    n2 = len(DNA2)
    dp = [ [-1 for j in range(n2)] for i in range(n1)] 
    return dna_match_topdown_recursion(DNA1, DNA2, n1-1, n2-1, dp)

def dna_match_bottomup(DNA1, DNA2):
	n1 = len(DNA1)
	n2 = len(DNA2)
	dp = [[-1 for j in range(n2 + 1)] for i in range(n1 + 1)]

	for i in range(n1 + 1):
		dp[i][0] = 0

	for j in range(n2 + 1):
		dp[0][j] = 0 

	for ind1 in range(1, n1 + 1):
		for ind2 in range(1, n2 + 1):
			if DNA1[ind1 - 1] == DNA2[ind2 - 1]:
				dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]

			else:
				dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

	return dp[n1][n2]