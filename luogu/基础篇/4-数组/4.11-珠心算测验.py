n = int(input())
a = list(map(int, input().split()))

b = []

for i in range(n):
    for j in range(i + 1, n):
        s = a[i] + a[j]
        if s in a and s not in b:
            b.append(s)

print(len(b))
