s=str(input())
c=input()
q=list()
w=list()
for i in range(len(s)):
    if s[i]==c:
        q.append(i)

for i in range(len(s)):
    t=list()
    for j in q:
        t.append(abs(i-j))

    w.append(min(t))

print(w)