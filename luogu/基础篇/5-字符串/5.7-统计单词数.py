word = input().lower()
passage = input().lower()

# 统计完整单词出现的次数
count = passage.split().count(word)

# 查找完整单词第一次出现的位置
pos = (" " + passage + " ").find(" " + word + " ")

if count == 0:
    print(-1)
else:
    print(count, pos)