def find_triangles(nums): #O(n^2)
    nums.sort()
    ans=0
    for i in range(len(nums)-2):
        first=i+1
        second=first+1
        while first<len(nums)-1:
            if nums[first]+nums[i]<=nums[second]:
                print(i,first,second)
                ans+=second-first-1
                first+=1
            else:
                if second<len(nums)-1:
                    second+=1
                else:
                    print(second)
                    if nums[second]<nums[first]+nums[i]:
                        ans+=second-first
                    first+=1
    return ans
a=[2,2,3,4]
print(find_triangles(a))

def CountTriangles(A):  #O(n^2)
    n = len(A)
    A.sort()
    count = 0
    for i in range(n - 1, 0, -1):
        l = 0
        r = i - 1
        while (l < r):
            if (A[l] + A[r] > A[i]):
                # If it is possible with a[l], a[r]
                # and a[i] then it is also possible
                # with a[l + 1]..a[r-1], a[r] and a[i]
                count += r - l
                # checking for more possible solutions
                r -= 1
            else:
                # if not possible check for
                # higher values of arr[l]
                l += 1
    print("No. of possible solutions: ", count)

# Driver Code
A = [4, 3, 5, 7, 6]

print(CountTriangles(A))