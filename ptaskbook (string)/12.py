A = input()
N = int(input())
AN = ''
for i in range(len(A)):
    AN += A[i]
    AN += '*' * N
print(AN)
