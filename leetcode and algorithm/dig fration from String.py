s='2/3chafr12/20'
index=[]
ans=[]
for i in range(len(s)):
    if s[i]=="/":
        index.append(i)
for i in range(len(index)):
    p1=index[i]-1
    p2=index[i]+1
    while 1:
        if s[p1]>='0' and s[p1]<='9' and p1>=0:
            p1-=1
        else:
            break
    while 1:
        if p2<len(s) and s[p2]>='0' and s[p2]<='9':
            p2+=1
        else:
            break
    print(s[p1+1:index[i]])
    norminator=int(s[p1+1:index[i]])
    denorminator=int(s[index[i]+1:p2])
    ans.append(round(norminator/denorminator,2))
print(ans)