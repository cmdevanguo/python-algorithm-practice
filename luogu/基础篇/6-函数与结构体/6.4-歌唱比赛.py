def score(marks):
    return (sum(marks) - max(marks) - min(marks)) / (len(marks) - 2)

def main():
    n, m = map(int, input().split())
    best = 0
    for _ in range(n):
        marks = list(map(int, input().split()))
        best = max(best, score(marks))
    print(f"{best:.2f}")

main()