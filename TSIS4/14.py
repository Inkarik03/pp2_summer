import re
s=str(input())
c=str(input())
q=list()
w=list()
x=re.search(c,s)
while re.search(c,s)!=None:
    x = re.search(c, s)
    a=x.start()
    b=x.end()
    q.append(a)
    w.append(b-1)
    if b-a>=2:
        s=s[0:a]+"%"*(b-a-1)+s[b-1:len(s)]

    else:
        s = s[0:a] + "%" * (b - a) + s[b:len(s)]

if len(q)>=1:
    for i in range(len(q)):
        print("("+str(q[i])+",",str(w[i])+")")

else:
    print("(-1, -1)")

