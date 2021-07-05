#string='abcthkjcba', ans: 'abctcba'
def longestPalindromeSubseq(s: str) -> int:
    n = len(s)
    if s == s[::-1]:
        return n
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        new_dp = list(dp)
        dp[i] = 1
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[j] = 2 + new_dp[j - 1]
            elif dp[j - 1] > dp[j]:
                dp[j] = dp[j - 1]
    return dp[-1]
s='abctvcdcba'
print(longestPalindromeSubseq(s))