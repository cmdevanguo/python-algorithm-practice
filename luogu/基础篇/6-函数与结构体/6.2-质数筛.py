def is_prime(x):
    if x < 2:
        return False
    i = 2
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True


n = int(input())
a = list(map(int, input().split()))

result = []
for x in a:
    if is_prime(x):
        result.append(str(x))

print(" ".join(result))