n = int(input())
a = [input() for i in range(n)]
b = [input() for i in range(n)]

ans = 7

# 先判断旋转90、180、270度
c = a
for k in range(1, 4):
    d = []
    for i in range(n):
        s = ""
        for j in range(n):
            s += c[n-1-j][i]
        d.append(s)
    c = d

    if c == b:
        ans = min(ans, k)

# 判断左右翻转
c = [row[::-1] for row in a]

if c == b:
    ans = min(ans, 4)

# 判断翻转后再旋转
for k in range(3):
    d = []
    for i in range(n):
        s = ""
        for j in range(n):
            s += c[n-1-j][i]
        d.append(s)
    c = d

    if c == b:
        ans = min(ans, 5)

# 判断是否不变
if a == b:
    ans = min(ans, 6)

print(ans)