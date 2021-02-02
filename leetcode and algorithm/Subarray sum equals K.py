# Given an array of integers nums and an integer k,
# return the total number of continuous subarrays whose sum equals to k.
# https://leetcode.com/problems/subarray-sum-equals-k/

#hashmap method. O(n)
class Solution:
    def subarraySum(self, nums, k: int) -> int:
        dic={}
        dic[0]=1
        sum=0
        ans=0
        for i in nums:
            sum+=i
            if (sum-k) in dic:
                ans+=dic[sum-k]
            dic[sum]=dic.get(sum,0)+1
        return ans
input=[1,2,3,-1,4]
print(Solution().subarraySum(input,3))