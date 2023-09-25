def checkSigns(n, arr):
    counter = 0
    for i in range(n):
        if arr[i] <0:
            counter += 1
    return counter

def max_independent_set_helper(n, arr, dp):
    if n == 0:
        return []
    elif n == 1:
        return [arr[0]] if arr[0] >= 0 else []
    else:   
        dp[0] = arr[0] if arr[0] >= 0 else 0
        dp[1] = max(dp[0], arr[1])

        for i in range(2, n):
            if arr[i] < 0:
                i += 1
            else:
                pick = arr[i] + dp[i-2]
                
                non_pick = 0 + dp[i-1]

                dp[i] = max(pick, non_pick)

        result = []
        i = n - 1
        while i >= 0:
            if dp[i] < 0:
                i -=1 
            else:     
                if dp[i] == dp[i-2] + arr[i] and dp[i]>=dp[i-1] or dp[i] == arr[i]:
                    result.append(arr[i])
                    i -= 2 
                else:
                    i -= 1
        result.reverse()

        return result 

def max_independent_set(nums):

    n = len(nums)

    if checkSigns(n, nums) == n:
        return []
    else:
        dp = [0 for _ in range(n)]
        return max_independent_set_helper(n, nums, dp)
