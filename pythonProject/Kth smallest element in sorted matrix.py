#leetcode 378 Kth smallest Element in sorted matrix
from queue import PriorityQueue
matrix=[[1,  5,  9],
        [10, 11, 13],
        [12, 13, 15]]
def kthSmallest(matrix,k):
    pq=PriorityQueue()
    for j in range(len(matrix)):
        pq.put([matrix[0][j],0,j])
    for i in range(k-1):
        p=pq.get()
        if p[1]==len(matrix)-1:
            continue
        pq.put([matrix[p[1]+1][p[2]],p[1]+1,p[2]])
    p=pq.get()
    return matrix[p[1]][p[2]]
print(kthSmallest(matrix,8))