def matrix_chain_order(dims):
    n = len(dims) - 1
    m = [[0] * (n + 1) for _ in range(n + 1)]
    s = [[0] * (n + 1) for _ in range(n + 1)]

    for length in range(2, n + 1):
        for i in range(1, n - length + 2):
            j = i + length - 1
            m[i][j] = float('inf')

            for k in range(i, j):
                cost = m[i][k] + m[k + 1][j] + dims[i - 1] * dims[k] * dims[j]

                if cost < m[i][j]:
                    m[i][j] = cost
                    s[i][j] = k

    return m, s


def print_optimal(s, i, j):
    if i == j:
        return f"A{i}"

    k = s[i][j]
    left = print_optimal(s, i, k)
    right = print_optimal(s, k + 1, j)

    return f"({left} x {right})"


dims = [10, 30, 5, 60, 10]

m, s = matrix_chain_order(dims)
n = len(dims) - 1

print("Minimum scalar multiplications:", m[1][n])
print("Optimal parenthesization:", print_optimal(s, 1, n))