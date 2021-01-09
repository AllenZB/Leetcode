def combine( n, k):
    stack = []
    res = []
    l, x = 0, 1
    while True:

        if l == k:
            res.append(stack[:])
        if l == k or n - x + 1 < k - l:
            if not stack:
                return res
            x = stack.pop() + 1
            l -= 1
        else:
            stack.append(x)
            x += 1
            l += 1
    return res
print(combine(5,3))
