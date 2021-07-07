import re
s=str(input())
g=re.findall(r"\d+", s)
y=int(g[0])
m=int(g[1])
d=int(g[2])

if len(g[1])!=2 or len(g[2])!=2:
    print("NO")

elif m>12 or d>31:
    print("NO")

elif d%400==0 or (d%100!=0 and d%4==0):
    if m==2:
        if d>29:
            print("NO")
        else:
            print("YES")

    elif (m<8 and m%2==1) or (m>7 and m%2==0):
        if d>31:
            print("NO")
        else:
            print("YES")

    else:
        if d>30:
            print("NO")
        else:
            print("YES")

else:
    if m == 2:
        if d > 28:
            print("NO")
        else:
            print("YES")

    elif (m < 8 and m % 2 == 1) or (m > 7 and m % 2 == 0):
        if d > 31:
            print("NO")
        else:
            print("YES")

    else:
        if d > 30:
            print("NO")
        else:
            print("YES")
