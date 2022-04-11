C = input()
k = 0
for i in range(len(C)):
    if 65 <= ord(C[i]) <= 90:
        k += 1
print(k)