a = [int(i) for i in input().split()]
n = 0
for i in a:
    if i > 0:
        n += 1
print(n)