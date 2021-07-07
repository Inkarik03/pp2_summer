s=input().split()
d= dict()

for i in s:
    try:
        d[i]+=1
    except KeyError:
        d[i]=1

f=sorted(d)
for i in f:
    print(i, d[i])