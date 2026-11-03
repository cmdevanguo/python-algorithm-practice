a = list(map(int, input().split()))

n = a[0]
s = ""

for i in range(1, len(a)):
    if i % 2 == 1:
        s += "0" * a[i]
    else:
        s += "1" * a[i]

for i in range(n):
    print(s[i*n:(i+1)*n])