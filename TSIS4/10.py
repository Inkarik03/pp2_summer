q=input().split()
cnt=0
for i in range(len(q)):
    for j in range(i+1, len(q)):
        if q[i]==q[j]:
            cnt+=1

print(cnt)