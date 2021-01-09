A=[1,2,3,1,4,2,5,3]
left_max=0
right_max=0
p1=0
p2=len(A)-1
ans=0
while p1<p2:
    left_max=max(left_max,A[p1])
    right_max=max(right_max,A[p2])
    current_min=min(left_max,right_max)
    if left_max<right_max:
        if A[p1]<current_min:
            ans+=current_min-A[p1]
        p1+=1
    else:
        if A[p2]<current_min:
            ans+=current_min-A[p2]
        p2-=1
print(ans)