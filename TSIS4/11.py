a=input().split()
b=input().split()
t=int(input())
x=list(zip(a,b))
r=0
for i in x:
    if int(i[1])>=t:
        r+=1

print(r)
