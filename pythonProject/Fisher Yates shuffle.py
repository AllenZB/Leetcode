
# shuffle an array randomly
# select index k from the back, random select an index from range(0,k-1), swap them.
from random import randint
a=[1,2,3,4,5,6,7,8,9]
for i in range(1,len(a)):
    j=len(a)-i
    k=randint(0,j)
    a[j],a[k]=a[k],a[j]
print(a)