def permuteUnique(nums):
    ans = []

    def recur(index):
        if index == len(nums) - 1:
            ans.append(list(nums))
        s = set()
        for i in range(index, len(nums)):
            if nums[i] in s:
                continue
            s.add(nums[i])
            nums[index], nums[i] = nums[i], nums[index]
            recur(index + 1)
            nums[index], nums[i] = nums[i], nums[index]
    recur(0)
    return ans
a=[1,2,2,2]
print(permuteUnique(a))