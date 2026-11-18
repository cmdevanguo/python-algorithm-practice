# 定义函数，计算两点之间的距离
def distance(x1, y1, x2, y2):
    return ((x2 - x1)**2 + (y2 - y1)**2)**0.5

# 输入三个点的坐标
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())
x3, y3 = map(float, input().split())

# 计算三条边
a = distance(x1, y1, x2, y2)
b = distance(x2, y2, x3, y3)
c = distance(x3, y3, x1, y1)

# 输出周长
print("%.2f" % (a + b + c))