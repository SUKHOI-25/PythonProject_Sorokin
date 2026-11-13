c = (input())
s = (input())
res = ""
print(f"{c},\n{s}")
for i in s:
    if c == i:
        res+= i*2
    else:
        res+=i
print(res)
        