n = input()
s = n

for i in range(len(n) - 1):
    s += input()

ans = [len(n)]
count = 0
current = "0"

for x in s:
    if x == current:
        count += 1
    else:
        ans.append(count)
        count = 1
        current = x

ans.append(count)
print(*ans)