n = int(input())

for x in range(10**n, 10**(n - 1) - 1, -1):
    if x % 2 != 0:
        print(x)