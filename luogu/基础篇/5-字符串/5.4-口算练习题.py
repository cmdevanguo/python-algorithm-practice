n = int(input())
# 记录当前的运算类型
op = ''
for k in range(n):
    # 按空格拆分这一行
    s = input().split()
    # 三个数据：第一个是运算类型
    if len(s) == 3:
        op = s[0]
        x = s[1]
        y = s[2]
    # 两个数据：沿用上一题的运算类型
    else:
        x = s[0]
        y = s[1]

    a = int(x)
    b = int(y)

    if op == 'a':
        e = x + '+' + y + '=' + str(a + b)
    elif op == 'b':
        e = x + '-' + y + '=' + str(a - b)
    else:
        e = x + '*' + y + '=' + str(a * b)

    print(e)
    print(len(e))