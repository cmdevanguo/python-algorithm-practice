n = int(input())
s = input().strip()

# 不做任何改变
ans = s.count("VK")

for i in range(n):
    # 换成另一个字符
    c = 'K' if s[i] == 'V' else 'V'
    # 字符串切片拼接出新串
    t = s[:i] + c + s[i+1:]
    ans = max(ans, t.count("VK"))

print(ans)