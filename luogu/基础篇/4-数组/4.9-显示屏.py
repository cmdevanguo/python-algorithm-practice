
n = int(input())
s = input()

a = [
    ["XXX", "X.X", "X.X", "X.X", "XXX"],  # 0
    ["..X", "..X", "..X", "..X", "..X"],  # 1
    ["XXX", "..X", "XXX", "X..", "XXX"],  # 2
    ["XXX", "..X", "XXX", "..X", "XXX"],  # 3
    ["X.X", "X.X", "XXX", "..X", "..X"],  # 4
    ["XXX", "X..", "XXX", "..X", "XXX"],  # 5
    ["XXX", "X..", "XXX", "X.X", "XXX"],  # 6
    ["XXX", "..X", "..X", "..X", "..X"],  # 7
    ["XXX", "X.X", "XXX", "X.X", "XXX"],  # 8
    ["XXX", "X.X", "XXX", "..X", "XXX"]   # 9
]

for i in range(5):
    for j in range(n):
        x = int(s[j])
        print(a[x][i], end="")
        if j != n - 1:
            print(".", end="")
    print()