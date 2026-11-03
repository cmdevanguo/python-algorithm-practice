n = int(input())

lights = [0] * 2000001

for i in range(n):
    a, t = input().split()
    a = int(a.replace('.', '')) # 精度问题
    t = int(t)

    for j in range(1, t + 1):
        x = a * j // 1000000 # 精度问题
        lights[x] = 1 - lights[x]

for i in range(len(lights)):
    if lights[i] == 1:
        print(i)
        break