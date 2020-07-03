
def lcs(x, y):
    if len(x) == 0 or len(y) == 0:
        return 0
    if x[0] == y[0]:
        return lcs(x[1:], y[1:]) + 1
    else:
        return max(lcs(x[1:], y), lcs(x, y[1:]))


if __name__ == '__main__':
    l = lcs('A周锋和朱芳雨。', 'A周鹏，朱芳雨')
    print(l)
