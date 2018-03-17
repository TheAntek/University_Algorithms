from operator import mul, sub


def column(row):
    i = 0
    n = len(row)
    while not row[i] and i < n:
        i += 1
    return i if i < n else -1


def gauss(les):
    """ Решение методом Гауса """

    n = len(les)
    m = les[:]

    indexes = [0 for _ in range(n)]

    for i in range(n):
        k = column(m[i])
        m[i] = [m[i][j] / m[i][k] for j in range(n + 1)]
        for j in (x for x in range(n) if x != i):
            m[j] = tuple(map(sub, m[j], map(mul, m[i], [m[j][k]] * (n + 1))))
        indexes[i] = k

    return [m[indexes[i]][n] for i in range(n)]


if "__main__" == __name__:
    a = tuple([int(input()) for i in range(4)])
    b = tuple([int(input()) for i in range(4)])
    c = tuple([int(input()) for i in range(4)])

    matrix = [a, b, c]
    # matrix = [(1, -3, 2, 1), (3, -4, 0, 2), (2, -5, 3, 2)]

    print(gauss(matrix))
