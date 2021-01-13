def subset_without_duplicate(nums):
    ans = [[]]
    nums.sort()
    for i in range(len(nums)):
        if i == 0 or nums[i] != nums[i - 1]:
            l = len(ans)
        for j in range(len(ans) - l, len(ans)):
            ans.append(ans[j] + [nums[i]])
    return ans
nums=[1,1,2,2]
print(subset_without_duplicate(nums))
#[[], [1], [1, 1], [2], [1, 2], [1, 1, 2], [2, 2], [1, 2, 2], [1, 1, 2, 2]]