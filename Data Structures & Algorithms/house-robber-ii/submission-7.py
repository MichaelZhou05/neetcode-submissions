def robLine(arr):
    if len(arr) == 1:
        return arr[0]

    dp = [0] * (len(arr) + 1)
    dp[1] = arr[0]

    for i in range(2, len(arr) + 1):
        dp[i] = max(dp[i-1], arr[i-1] + dp[i-2])

    return dp[-1]