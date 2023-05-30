
## WAP to print unique charecters in a given string??

s="ttuushaarr"
d={}
for i in s:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
for j in d:
    if d[j]==1:
        print(j)

