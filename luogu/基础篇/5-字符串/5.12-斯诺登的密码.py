# 普通数字单词
num_words = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty".split()

# 特殊单词
special_words = "a both another first second third".split()

# 将两组单词合并
words_list = num_words + special_words

# 对应的数字
num_list = list(range(21)) + [1, 2, 1, 1, 2, 3]

# 输入句子并转换为小写
s = input().lower()

# 按空格拆分
words = s.split()

# 保存计算结果
ans = []

for word in words:
    # 去掉句号
    word = word.rstrip(".")

    # 判断单词是否存在
    if word in words_list:
        # 获取单词对应的数字
        x = num_list[words_list.index(word)]

        # 平方后对100取模，转换为两位字符串
        y = str(x * x % 100).zfill(2)

        ans.append(y)

# 字符串升序排序
ans.sort()

# 拼接所有字符串
result = "".join(ans)

# 去掉开头的0
result = result.lstrip("0")

# 输出结果
if result == "":
    print(0)
else:
    print(int(result))