#find all k-combinations from range(1,n+1)
#Approach1: backtrack
def combine(n, k):
    stack = []
    res = []
    l, x = 0, 1     # l is the length of the combination. x is the next value will be added to the combination
    while True:

        if l == k:
            res.append(stack[:])
        if l == k or n - x + 1 < k - l:   # we need k-l more numbers, n-x+1 is the remaining numbers
            if not stack:
                return res
            x = stack.pop() + 1       
            l -= 1
        else:
            stack.append(x)
            x += 1
            l += 1
    return res

combine(5,3)



#Approach2: dfs:
def combine(n, k):
    stack = []
    res = []
    l, x = 0, 1     # l is the length of the combination. x is the next value will be added to the combination
    while True:

        if l == k:
            res.append(stack[:])
        if l == k or n - x + 1 < k - l:   # we need k-l more numbers, n-x+1 is the remaining numbers
            if not stack:
                return res
            x = stack.pop() + 1
            l -= 1
        else:
            stack.append(x)
            x += 1
            l += 1
    return res

#Find all the combination in a list candidates->list[int], that sum to target
#store the combination that sum to i into ans[i]
def combinationSum(candidates, target: int) :
    ans = [[] for i in range(target + 1)]
    ans[0] = [[]]
    for candidate in candidates:
        for i in range(target - candidate + 1):
            for path in ans[i]:
                ans[i + candidate].append(path + [candidate])
    return ans[-1]
