#find all k-combinations from range(1,n+1)
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
combine(5,3)