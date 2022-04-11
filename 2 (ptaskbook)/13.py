a = int(input())
b = int(input())
c = int(input())
if c < a < b:
    if b < a < c:
        print(a)
    else:
        print(c)
else:
    if a < b < c:
        print(b)
    else:
        print(c)