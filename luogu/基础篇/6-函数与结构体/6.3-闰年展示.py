def is_leap(year):
    return (year % 4 == 0 and year % 100 != 0) or year % 400 == 0

def main():
    x, y = map(int, input().split())

    leap_years = []
    for year in range(x, y + 1):
        if is_leap(year):
            leap_years.append(year)

    print(len(leap_years))
    print(' '.join(map(str, leap_years)))

main()