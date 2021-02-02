"""
Input: nums = [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
"""
#method 1, dp, O(n)
a=[10,9,2,5,3,7,101,18]
def find_longest(nums):
    dp=[1]*len(nums)
    for i in range(len(nums)-1,-1,-1):
        for j in range(i+1,len(nums)):
            if nums[i]<nums[j]:
                dp[i]=max(dp[i],dp[j]+1)
    return max(dp)
print("dp: ",end='')
print(find_longest(a))

# method 2, dp+binary search, O(Nlog(N)), Patience sorting
def LIS(nums):
    tail=[0]*len(nums)
    size=0
    for x in nums:
        i,j=0,size
        while i!=j:
            m=(i+j)//2
            if tail[m]<x:
                i=m+1
            else:
                j=m
        tail[i]=x
        size=max(i+1,size)
    return size
print("dp+binary: ",end='')
print(LIS(a))