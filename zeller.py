
def zeller(year, month, day):
    c = year // 100
    y = year % 100
    m = month
    d = day
    y = y + (m + 9) // 12 - 1
    m = (m + 9) % 12 + 3
    return (c // 4 - 2 * c + y + y // 4 + 13 * (m + 1) // 5 + d - 1) % 7


if __name__ == '__main__':
    w = zeller(2020, 1, 26)
    print(w)
