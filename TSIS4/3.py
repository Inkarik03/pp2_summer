import re

s = int(input())
a=[]
for i in range(s):
    l = input()
    a.append(l)

for i in a:
    x=re.findall(r"[A-Za-z]+\s<[A-Za-z][\w!+_.-]+@[a-z]+\.[a-z][a-z]?[a-z]?>",i)
    if x:
        print(*x)