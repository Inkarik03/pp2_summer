import re

n=int(input())
a=""
g=1
res = r"(#([0-9a-fA-F]){3}([0-9a-fA-F]?){3})"
for i in range(n-1):
    c=str(input())
    if c=="}":
        g=1

    if len(c)>=1:
        if c[len(c)-1]=="{":
            g=0
            continue
    if g==0:
        a+=c

result = re.findall(r".+", a)
x=re.findall(res,result[0])
for i in x:
    print(str(i[0]))