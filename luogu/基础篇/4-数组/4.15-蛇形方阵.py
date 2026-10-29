n = int(input())
a = [[0] * n for _ in range(n)]

i, j = 0, 0
dx, dy = 0, 1  # 初始向右

for c in range(1, n * n + 1):
    a[i][j] = c

    x, y = i + dx, j + dy

    if not (0 <= x < n and 0 <= y < n) or a[x][y] != 0:
        dx, dy = dy, -dx

    i += dx
    j += dy

for row in a:
    for x in row:
        print(f"{x:3d}", end="")
    print()