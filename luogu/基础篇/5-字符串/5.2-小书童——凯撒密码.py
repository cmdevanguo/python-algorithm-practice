n = int(input())
s = input()

ans = ""

for c in s:
    x = (ord(c) - ord('a') + n) % 26
    ans += chr(x + ord('a'))

print(ans)