a = input()
b = input()

x = 1
y = 1

for i in a:
    x = x * (ord(i) - ord('A') + 1)

for i in b:
    y = y * (ord(i) - ord('A') + 1)

if x % 47 == y % 47:
    print("GO")
else:
    print("STAY")