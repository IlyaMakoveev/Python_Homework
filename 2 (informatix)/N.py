n = int(input())
m = n % 60
h = n % (60 * 24) // 60
print(h, m)