b = input()
a = [int(b) for b in b.split()]
for i in a:
    if int(i)%2 != 0:
       a[i] = i
a.sort()
print(a[1])