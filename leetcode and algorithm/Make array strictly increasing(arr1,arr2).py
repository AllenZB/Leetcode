import collections
import bisect
class Solution:
    def makeArrayIncreasing(self, arr1, arr2) -> int:
        dp = {-1:0}
        arr2.sort()
        for num in arr1: #O(n^2)
            tmp = collections.defaultdict(lambda: float('inf'))
            for key in dp:
                if num > key:
                    tmp[num] = min(tmp[num],dp[key])
                loc = bisect.bisect_right(arr2,key)
                if loc < len(arr2):
                    tmp[arr2[loc]] = min(tmp[arr2[loc]],dp[key]+1)
            dp = tmp
        if dp:
            return min(dp.values())
        return -1
arr1 = [1,5,3,6,7]
arr2 = [4,3]      #ans: arr1=[1,3,4,6,7] ,minimum 2 operations to make arr1 strictly increasing
print(Solution().makeArrayIncreasing(arr1,arr2))