import re
n=int(input())
d={'a':0, 'b':0, 'c':0}
for i in range(n):
    s= input().split()
    x= re.findall(r"[A-Z]", s[0])
    d['a']+=len(x)
    v= re.findall(r"[0-9]", s[2])
    d['c']+=len(v)
    h=re.findall("[aeuio]", s[1])
    d['b']+=len(h)

print(d)