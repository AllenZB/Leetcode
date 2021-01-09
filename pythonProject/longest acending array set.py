a=[4,300,1,3,2,7] #return [1,2,3,4]
ans=0
dic={}
s=set()
start=0
end=0
for i in a:
    s.add(i)
    dic[i]=False
for i in a:
    if dic[i]==False:
        m=i
        n=i+1
        while m in s and dic[m]==False:
            dic[m] = True
            m-=1
        while n in s and dic[n]==False:
            dic[n] = True
            n+=1
        if n-m>ans:
            ans=n-m
            start=m+1
            end=n-1
print(start,end)
