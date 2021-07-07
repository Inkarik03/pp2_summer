import re

n=int(input())
lookfor = r"^[+-]?([\d]*)?\.{1}([0-9]+)$"

for i in range(n):
    c=str(input())
    x=re.search(lookfor, c)
    if x:
        print("True")
    else:
        print("False")