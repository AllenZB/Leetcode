#Manacher algorithm, get the longest palindromic in O(n)
#https://segmentfault.com/a/1190000008484167
s="abcba"
s_new="$#"
#initialize to "$#a#b#c#b#a#^"
for i in s:
    s_new+=i
    s_new+="#"
s_new+="^"
max_len=-1
id=1
mx=0
p=[1 for i in range(len(s_new))]
for i in range(1,len(s_new)-1):
    if i<mx:
        p[i]=min(p[2*id-i],mx-i)
    else:
        p[i]=1
    while s_new[i-p[i]]==s_new[i+p[i]]:
        p[i]+=1
    if i+p[i]>mx:
        id=i
        mx=i+p[i]
    max_len=max(max_len,p[i]-1)
print(max_len)