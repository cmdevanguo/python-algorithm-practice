s = ""
for i in range(4):
    s += input()

cnt = [0] * 26

for c in s:
    if 'A' <= c <= 'Z':
        cnt[ord(c) - ord('A')] += 1

h = max(cnt)

for i in range(h, 0, -1):
    line = ""
    for j in range(26):
        if cnt[j] >= i:
            line += "* "
        else:
            line += "  "
    print(line.rstrip())

print(" ".join("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))