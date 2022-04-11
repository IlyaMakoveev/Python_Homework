a = [int(i) for i in input().split()]

a.sort()

for i in range(len(a)):
    if a[i] < a[i+1] and a[i] > 0:
        m = a[i]
        break
    if len(a) == 1 and a[0] > 0:
        print(a[0])
print(m)