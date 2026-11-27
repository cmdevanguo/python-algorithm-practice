def fate(i, j, full):
    """返回第 i 行第 j 列的人是否不被赦免"""
    return 1 if (i | j) == full else 0

def main():
    n = int(input())
    size = 2 ** n
    full = size - 1
    for i in range(size):
        print(" ".join(str(fate(i, j, full)) for j in range(size)))

main()