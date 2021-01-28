#given an array of numbers, you cannot take adjacent number, find the largest number you can take.
#classic dynamic programming

class Solution:
    def rob(self, nums) -> int:
        dp=[-1]*(len(nums)+1)
        def recur(index):
            if index<0:
                return 0
            if not dp[index]>=0:
                #essence
                result=max(recur(index-2)+nums[index],recur(index-1))
                dp[index]=result
            return dp[index]
        return recur(len(nums)-1)
a=[183,219,57,193,94,233,202,154,65,240,97,234,100,249,186,66,90,238,168,128,177,235,50,81,185,165,217,207,88,80,112,78,135,62,228,247,211]
print(Solution().rob(a))