"""超时了！！！"""
# m, n = map(int, input().split())
#
# a = [0] * 10
#
# for i in range(m, n + 1):
#     for j in str(i):
#         a[int(j)] += 1
#
# for i in range(10):
#     if i == 9:
#         print(a[i])
#     else:
#         print(a[i], end=" ")

"""优化"""

m, n = map(int, input().split())

a = [0] * 10

for t in range(2):
    if t == 0:
        x = n
        sign = 1
    else:
        x = m - 1
        sign = -1

    p = 1

    while p <= x:
        high = x // (p * 10)
        cur = (x // p) % 10
        low = x % p

        for i in range(10):
            if i == 0:
                if high == 0:
                    continue
                c = (high - 1) * p
            else:
                c = high * p

            if cur > i:
                c += p
            elif cur == i:
                c += low + 1

            a[i] += sign * c

        p *= 10

for i in range(10):
    if i == 9:
        print(a[i])
    else:
        print(a[i], end=" ")