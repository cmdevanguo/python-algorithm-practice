n, m, k = map(int, input().split())
a = [[0] * n for _ in range(n)]

# 火把
for _ in range(m):
    x, y = map(int, input().split())

    for i in range(-2, 3):
        for j in range(-2, 3):
            if abs(i) + abs(j) <= 2:
                nx = x - 1 + i
                ny = y - 1 + j

                if 0 <= nx < n and 0 <= ny < n:
                    a[nx][ny] = 1

# 萤石
for _ in range(k):
    x, y = map(int, input().split())

    for i in range(-2, 3):
        for j in range(-2, 3):
            nx = x - 1 + i
            ny = y - 1 + j

            if 0 <= nx < n and 0 <= ny < n:
                a[nx][ny] = 1

# 统计没有被照亮的位置
ans = 0
for row in a:
    for x in row:
        if x == 0:
            ans += 1

print(ans)