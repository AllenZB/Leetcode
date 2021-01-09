A=[[1,1,1,2,2],
   [1,1,2,3,3],
   [1,2,1,3,1],
   [1,1,1,2,2]]
ans=0
visited=[]
for i in range(len(A)):
    current=[]
    for j in range(len(A[0])):
        current.append(False)
    visited.append(current)
def find_area(i,j,value):
    if A[i][j]!=value:
        return
    visited[i][j]=True
    if i-1>=0 and not visited[i-1][j]:
        find_area(i-1,j,value)
    if i+1<len(A) and not visited[i+1][j]:
        find_area(i+1,j,value)
    if j+1<len(A[0]) and not visited[i][j+1]:
        find_area(i,j+1,value)
    if j-1>=0 and not visited[i][j-1]:
        find_area(i,j-1,value)
for i in range(len(A)):
    for j in range(len(A[i])):
        if not visited[i][j]:
            ans+=1
            find_area(i,j,A[i][j])
print(ans)