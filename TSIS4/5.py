import re

n = int(input())

for i in range(n):
    c=str(input())
    if len(c)==10:
        x=re.findall(r"[7-9][0-9]{9}",c)
        if x:
            print("YES")

        else:
            print("NO")

    else:
        print("NO")