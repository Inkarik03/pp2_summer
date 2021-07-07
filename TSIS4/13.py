import re

s = str(input())
x = re.findall(r"[aeiouAIEOU][aeiouAIEOU]+[QWRTPSDFGHJKLZXCVBNMqwrtpsdfghjklzxcvbnm]", s)
if x:
    for i in x:
        print(i[0:len(i)-1])

else:
    print(-1)
