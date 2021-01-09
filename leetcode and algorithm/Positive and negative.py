A=[1,2,3,-1,-2,-3,1,-2]
flag=False
A.sort()
p1=1
p2=len(A)-1
while p1<p2:
    if (A[p1]<0 and A[p2]<0) or (A[p1]>0 and A[p2]>0):
        break
    A[p1],A[p2]=A[p2],A[p1]
    p1+=1
    p2-=1
    if flag:
        if A[p1]<0:
            p2=len(A)-1
            flag=False
        else:
            p1+=1
    elif flag==False and A[p1]>0:
         p2=len(A)-1
         flag=True
    else:
        p1+=1
print(A)