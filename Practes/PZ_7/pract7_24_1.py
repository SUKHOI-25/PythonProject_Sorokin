s = input()
a = s.split()
print(a)
count = 0
for i in range(len(a)):
    if a[i]=='AAA' or a[i]=='ААА':
        count += 1
print(count)