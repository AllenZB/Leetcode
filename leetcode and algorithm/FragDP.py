# leetcode 1824
def minSideJumps(obstacles):
    dp=[1,0,1]
    for val in obstacles:
        if val:
            dp[val-1]=float('inf')
        for i in range(3):
            if i!=val-1:
                dp[i]=min(dp[i],dp[(i+1)%3]+1,dp[(i+2)%3]+1)
    return min(dp)
