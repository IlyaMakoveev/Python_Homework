C = input()
k = 0
for i in range(len(C)):
    if 48 <= ord(C[i]) <= 57:
        k += 1
print(k)
