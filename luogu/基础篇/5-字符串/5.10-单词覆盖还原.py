s = input()

boy = 0
girl = 0

for i in range(len(s) - 2):
    if s[i] == 'b' or s[i + 1] == 'o' or s[i + 2] == 'y':
        boy += 1

for i in range(len(s) - 3):
    if s[i] == 'g' or s[i + 1] == 'i' or s[i + 2] == 'r' or s[i + 3] == 'l':
        girl += 1

print(boy)
print(girl)