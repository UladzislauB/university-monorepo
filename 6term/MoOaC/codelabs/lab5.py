import numpy as np


def find_optimal_transport_plan(a, b, C):
    m, n = get_length(a, b)

    difference = sum(a) - sum(b)
    if difference != 0:
        make_correction(a, b, m, n, C, difference)
        m, n = get_length(a, b)

    X, U_basis = nord_west_method(a, b)

    while True:
        u, v = get_potentials(C, U_basis)
        U_basis_matrix = get_Ub_matrix(m, n, U_basis)

        for i, j in i_j_generator(m, n):
            if U_basis_matrix[i][j] == 0 and u[i] + v[j] > C[i][j]:
                U_basis_matrix[i][j] = 1
                U_basis.append((i, j))
                break
        else:
            print(X)
            return

        rows_basis, columns_basis = rebuild_Ub(m, n, U_basis)

        loop = []
        loop.append((i, j))

        make_sifting(rows_basis, columns_basis)

        up = True
        i, j = loop[0]
        while True:
            if up:
                up = False
                i = columns_basis[j][1] if columns_basis[j][0] == i else columns_basis[j][0]
            else:
                up = True
                j = rows_basis[i][1] if rows_basis[i][0] == j else rows_basis[i][0]
            if i == loop[0][0] and j == loop[0][1]:
                break
            else:
                loop.append((i, j))

        delete_cycle(X, loop, U_basis, m, n)


def nord_west_method(a, b):
    m, n = get_length(a, b)
    X = [[0] * n for _ in range(m)]
    i, j = 0, 0
    Ub = []

    while True:
        Ub.append((i, j))
        max_supply = min(a[i], b[j])
        a[i] -= max_supply
        b[j] -= max_supply
        X[i][j] = max_supply
        if i == m - 1 and j == n - 1:
            break
        if a[i] == 0 and i < m:
            i += 1
        elif b[j] == 0 and j < n:
            j += 1

    return X, Ub


def get_potentials(C, Ub):
    m = len(C)
    n = len(C[0])
    A = [[0] * (n + m) for _ in range(n + m)]
    b = [0] * (n + m)

    A[-1][0] = 1
    b[-1] = 0

    for it_num, (i, j) in enumerate(Ub):
        A[it_num][i] = A[it_num][m + j] = 1
        b[it_num] = C[i][j]

    x = np.linalg.solve(A, b)
    return x[:m], x[m:]


def rebuild_Ub(m, n, Ub):
    rows_basis, columns_basis = [[] for _ in range(m)], [[] for _ in range(n)]

    for i, j in Ub:
        rows_basis[i].append(j)
        columns_basis[j].append(i)
    return rows_basis, columns_basis


def get_Ub_matrix(m, n, Ub):
    Ub_matrix = [[0] * n for _ in range(m)]
    for i, j in Ub:
        Ub_matrix[i][j] = 1

    return Ub_matrix


def i_j_generator(n, m):
    for i in range(n):
        for j in range(m):
            yield i, j


def make_correction(a, b, m, n, C, difference):
    if difference > 0:
        b.append(difference)
        n += 1
        for row in C:
            row.append(0)
    elif difference < 0:
        a.append(-difference)
        m += 1
        C.append([0] * n)


def get_length(a, b):
    return len(a), len(b)


def make_sifting(rows_basis, columns_basis):
    deleted = True

    while deleted:
        deleted = False
        for i, row in enumerate(rows_basis):
            if len(row) < 2:
                for j in row:
                    columns_basis[j].remove(i)
                    deleted = True
                row.clear()
        for j, column in enumerate(columns_basis):
            if len(column) < 2:
                for i in column:
                    rows_basis[i].remove(j)
                    deleted = True
                column.clear()


def delete_cycle(X, loop, U_basis, m, n):
    theta = min(X[loop[i][0]][loop[i][1]] for i in range(1, len(loop), 2))
    coefficient = 1
    for i, j in loop:
        X[i][j] += coefficient * theta
        if X[i][j] == 0 and len(U_basis) > n + m - 1 and coefficient == -1:
            U_basis.remove((i, j))
        coefficient = -1 if coefficient == 1 else 1


if __name__ == '__main__':
    a = [100, 300, 300]
    b = [300, 200, 200]
    C = [[8, 4, 1],
         [8, 4, 3],
         [9, 7, 5]]

    find_optimal_transport_plan(a, b, C)
