n = int(input())
k = int(input())

if 1 <= k <= n <= 50 and n % 2 == 0:
    if n == 2:
        x = 0
    elif k > n // 2:
        x = n - 3 - (n - k)
    elif k <= n // 2:
        x = n - 3 - (k - 1)

    print(x)
