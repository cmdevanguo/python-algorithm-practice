q = int(input())
s = input().strip() # 删除字符串开头和结尾的空白字符（不加这个会报'read (ASCII 13), expected ~'）

for i in range(q):
    line = input().strip() # 删除字符串开头和结尾的空白字符（不加这个会报'read (ASCII 13), expected ~'）
    # 第一个字符就是操作编号
    op = line[0]
    # 去掉 "x " 后剩下的部分
    rest = line[2:]

    # 后接插入
    if op == '1':
        s = s + rest
        print(s)
    # 截取：从第 a 个字符起取 b 个
    elif op == '2':
        p = rest.find(' ') # 在字符串 rest 里找空格 ' '，返回它第一次出现的位置（下标）
        a = int(rest[:p])
        b = int(rest[p + 1:])
        s = s[a:a + b]
        print(s)
    # 在第 a 个字符前插入
    elif op == '3':
        p = rest.find(' ')
        a = int(rest[:p])
        t = rest[p + 1:]
        s = s[:a] + t + s[a:]
        print(s)
    # 查找子串
    else:
        print(s.find(rest))