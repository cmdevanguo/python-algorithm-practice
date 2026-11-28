def read_students():
    """读取输入，返回学生列表，每个元素为 (姓名, 语文, 数学, 英语)"""
    n = int(input())
    students = []
    for _ in range(n):
        parts = input().split()
        name = parts[0]
        chinese = int(parts[1])
        math = int(parts[2])
        english = int(parts[3])
        students.append((name, chinese, math, english))
    return students

def total_score(student):
    """计算一名学生的总分"""
    return student[1] + student[2] + student[3]

def find_best(students):
    """找出总分最高的学生；总分相同时保留靠前的"""
    best = students[0]
    for s in students[1:]:
        if total_score(s) > total_score(best):  # 严格大于，保证并列时取靠前者
            best = s
    return best

def main():
    students = read_students()
    best = find_best(students)
    print(*best)

main()