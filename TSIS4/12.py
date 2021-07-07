f=open("perfect.in.txt", "r")
g=open("perfect.out.txt", "w")
s=f.readline()
d=len(s)
q=1
for i in f:
    s=f.readline()
    if d<=len(s):
        d=s

    else:
        q=0
if q==0:
    g.write("NO")

else:
    g.write("YES")


