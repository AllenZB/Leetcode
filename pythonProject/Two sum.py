A=[1,2,3,4,5,6,7,8]
k=5
s=set()
ans=[]
for i in A:
    if i not in s:
        s.add(i)
for i in A:
    if k-i in s and [k-i,i] not in ans:
        ans.append([i,k-i])
print(ans)