#quickSort
a=[10,9,8,7,2,3,4,2,1]
def quickSort(low,high):
    if low<high:
        m=partition(low,high)
        quickSort(low,m-1)
        quickSort(m+1,high)
def partition(i,j):
    m=i
    pivot=a[i]
    for k in range(i+1,j+1):
        if a[k]<pivot:
            m+=1
            a[k],a[m]=a[m],a[k]
    a[i],a[m]=a[m],a[i]
    return m
quickSort(0,len(a)-1)
print(a)