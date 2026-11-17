s = input()
a = b = c = 0

for i in s.split(';'):
    if ':=' not in i:
        continue

    x, y = i.split(':=')

    if y == 'a':
        n = a
    elif y == 'b':
        n = b
    elif y == 'c':
        n = c
    else:
        n = int(y)

    if x == 'a':
        a = n
    elif x == 'b':
        b = n
    elif x == 'c':
        c = n

print(a, b, c)