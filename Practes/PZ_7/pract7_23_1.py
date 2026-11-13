s = input()
s=s.replace("--","+")
res = int(s[0])
for i in range(len(s)):
    if s[i]=="+":
        res+=int(s[i+1])
    elif s[i]=="-":
        res-=int(s[i+1])

print(res)