a = int(input())
b = int(input())
c = int(input())
if a > b:
    if a > c:
        m1 = a
    else:
        m1 = c
else:
    if b > c:
        m1 = b
    else:
        m1 = c

if c < a < b:
    if b < a < c:
        m2 = a
    else:
        m2 = c
else:
    if a < b < c:
        m2 = b
    else:
        m2 = c

print(m1 + m2)