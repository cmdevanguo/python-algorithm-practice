def fact(n):
    expr = "*".join(map(str, range(1, n + 1)))
    return eval(expr)

n = int(input())
print(fact(n))