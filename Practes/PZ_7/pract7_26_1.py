n1 = int(input())
n2 = int(input())

s1 = input()
s2 = input()

print(f"{n1}\n{n2}\n{s1}\n{s2}")
suprim = ""
print(s1[:n1]+s2[len(s2)-n2:])