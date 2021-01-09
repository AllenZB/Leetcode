#mergeSort
a=[10,9,8,6,8,3,4,2,1]

def mergeSort(low,high):
    if low<high:
        mid=(low+high)//2
        mergeSort(low,mid)
        mergeSort(mid+1,high)
        merge(low,mid,high)
def merge(low,mid,high):
    b=[]
    i=low
    j=mid+1
    while i<=mid and j<=high:
        if a[i]<a[j]:
            b.append(a[i])
            i+=1
        else:
            b.append(a[j])
            j+=1
    while i<=mid:
        b.append(a[i])
        i+=1
    while j<=high:
        b.append(a[j])
        j+=1
    for i in range(len(b)):
        a[low+i]=b[i]
mergeSort(0,len(a)-1)
print(a)