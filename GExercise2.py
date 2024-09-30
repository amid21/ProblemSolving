def solution(A):
    total_sum = sum(A)
    n = len(A)
    # dp[i] will be True is a subset with sum i is possible
    dp = [False] * (total_sum + 1)
    dp[0] = True

    for num in A: 
        # Traverse backwards to avoid overwriting
        for j in range(total_sum, num - 1, -1):
            if dp[j-num]:
                dp[j] = True
    # Find the min difference
    min_diff = float('inf')
    for s in range(total_sum // 2 + 1):
        if dp[s]:
            min_diff = min(min_diff, abs(total_sum - 2 * s))
    return min_diff

A = [2, 3, 6, 9]
print(solution(A))