n, m = map(int, input().split())

a = []
for i in range(n):
    a.append(int(input()))

ans = sum(a[:m])

for i in range(1, n - m + 1):
    s = sum(a[i:i + m])
    ans = min(ans, s)

print(ans)