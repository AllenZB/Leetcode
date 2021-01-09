#find the median in an unsorted array in linear time
import random
#Approach 1: Selection Algorithm, average complexity O(n), worst complexity O(n**2)
#It works as follows, select a pivot and partition the array to left and right subarrays such that,
# the elements that are smaller than the pivot value end up in the left group,
# and the ones that are and larger than or equal to the pivot are in the right group.
# Now, only the pivot is in its sorted position.
# The remaining elements are not sorted but their relative position to the pivot,
# whether they are on the left or right, is as in sorted order.
# Let’s say after partitioning the array the position of the pivot in the array is m.
# If m is equal to k, then the pivot is exactly the kth element that we’re looking for,
# so we return the pivot value. If m is less than k, then the kth element is in the right subarray.
# Else if m is greater than k, then the kth element is in the left subarray.
# So we can recursively call the same procedure and find the kth element.
def partition1(arr, left, right, pivotIndex):
    arr[right], arr[pivotIndex] = arr[pivotIndex], arr[right]
    pivot = arr[right]
    swapIndex = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            swapIndex += 1
    arr[right], arr[swapIndex] = arr[swapIndex], arr[right]
    return swapIndex


def kthLargest1(arr, left, right, k):
    if not 1 <= k <= len(arr):
        return
    if left == right:
        return arr[left]

    while True:
        pivotIndex = random.randint(left, right)
        pivotIndex = partition1(arr, left, right, pivotIndex)
        rank = pivotIndex - left + 1
        if rank == k:
            return arr[pivotIndex]
        elif k < rank:
            return kthLargest1(arr, left, pivotIndex - 1, k)
        else:
            return kthLargest1(arr, pivotIndex + 1, right, k - rank)


#Approach 2: Median of Medians: O(n)
#The algorithm divides the array to groups of size 5 (the last group can be of any size < 5).
# Then calculates the median of each group by sorting and selecting the middle element
# (sorting complexity of 5 elements is negligible). Finds the median of these medians by recursively
# calling itself, and selects the median of medians as the pivot for partition.
# Then it continues similar to the previous selection algorithm by
# recursively calling the left or right subarray depending on the rank of the pivot after partitioning.
# The partition function is slightly different though, partition1 function above takes the index of
# the pivot as input, partition2 here takes the value of the pivot as input, which is only a slight modification
def partition2(arr, left, right, pivot):
    swapIndex = left
    for i in range(left, right + 1):
        if arr[i] < pivot:
            arr[i], arr[swapIndex] = arr[swapIndex], arr[i]
            swapIndex += 1
    return swapIndex - 1


def kthLargest2(arr, left, right, k):
    length = right - left + 1
    if not 1 <= k <= length:
        return
    if length <= 5:
        return sorted(arr[left:right + 1])[k - 1]

    numMedians = length / 5
    medians = [kthLargest2(arr, left + 5 * i, left + 5 * (i + 1) - 1, 3) for i in range(numMedians)]
    pivot = kthLargest2(medians, 0, len(medians) - 1, len(medians) / 2 + 1)
    pivotIndex = partition2(arr, left, right, pivot)
    rank = pivotIndex - left + 1
    if k <= rank:
        return kthLargest2(arr, left, pivotIndex, k)
    else:
        return kthLargest2(arr, pivotIndex + 1, right, k - rank)