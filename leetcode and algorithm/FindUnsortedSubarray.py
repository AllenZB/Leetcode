#Input: nums = [2,6,4,8,10,9,15]
#Output: 5
#Explanation: You need to sort [6, 4, 8, 10, 9] in ascending order to make the whole array
# sorted in ascending order.
def findUnsortedSubarray(nums) :
    l, r = 0, len(nums) - 1
    min, max = 10001, -10001
    st, nd = 0, -1

    while r >= 0:
        if nums[l] >= max:
            max = nums[l]
        else:
            nd = l
        if nums[r] <= min:
            min = nums[r]
        else:
            st = r

        l += 1
        r -= 1

    return nd - st + 1