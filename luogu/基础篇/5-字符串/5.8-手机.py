s = input()
keys = ["abc", "def", "ghi", "jkl", "mno",
        "pqrs", "tuv", "wxyz"]

count = 0

for i in s:
    if i == " ":
        count += 1
    else:
        for key in keys:
            if i in key:
                count += key.find(i) + 1
                break

print(count)