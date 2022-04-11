a = int(input())
b = int(input())
c = int(input())
d = int(input())
a1 = abs(a - c)
b1 = abs(b - d)
if a1 == 1 and b1 == 2 or a1 == 2 and b1 == 1:
    print('YES')
else:
    print('NO')