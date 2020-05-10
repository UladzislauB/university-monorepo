import numpy as np

a = np.array([[1, 1, 1],
              [2, 2, 2]])

b = np.array([-1, 2])

c = np.array([])

n = 3

m = 2


def initial_phase_simplex_method(m, n, matrix_A, b, c):
    make_vector_b_positive(matrix_A, b)
    matrix_A_extended, x_extended, Jb, c_extended = \
        get_initial_canonical_additional_task(m, n, matrix_A, b)

    main_phase_simplex_method(matrix_A_extended, x_extended, Jb, c_extended)

    if next((index for index, value in enumerate(x_extended[n:]) if value != 0), -1) != -1:
        print("No solution")
        return

    x = x_extended[:n]
    l_list = get_l_from_j_list(n, Jb, matrix_A_extended)
    matrix_A, Jb = delete_excess_equations(n, Jb, l_list, matrix_A)

    print(Jb)
    print(matrix_A)


def make_vector_b_positive(matrix_A, b):
    for index, value in enumerate(b):
        if value < 0:
            matrix_A[index] *= -1
            b[index] *= -1


def get_initial_canonical_additional_task(m, n, matrix_A, b):
    x_extended = np.hstack((np.array([0] * n), np.copy(b)))
    matrix_A_extended = np.hstack((matrix_A, np.eye(m)))
    Jb = np.array([index + 1 for index in range(n, n + m)])
    c_extended = np.hstack(([0] * n, [-1] * m))
    return matrix_A_extended, x_extended, Jb, c_extended


def get_l_from_j_list(n, Jb, matrix_A_extended):
    transposed_matrix_a = np.array(get_transposed_matrix(matrix_A_extended))
    basis_matrix = np.array(get_basis_matrix(transposed_matrix_a, Jb))
    inverse_basis_matrix = np.linalg.inv(np.array(basis_matrix))
    return [get_l_from_j(inverse_basis_matrix, matrix_A_extended[:, j])
            for j in range(n) if j + 1 not in Jb]


def get_l_from_j(inverse_basis_matrix, column_j):
    return inverse_basis_matrix @ column_j


def delete_excess_equations(n, Jb, l_list, matrix_A):
    list_k = []
    list_i = []
    for index, value in enumerate(Jb):
        if value > n:
            k = index
            i = value - n

            delete_equation = True
            for vector in l_list:
                if vector[k] != 0:
                    Jb[k] = vector[k]
                    delete_equation = False
                    break
            if delete_equation:
                list_i.append(i)
                list_k.append(k)


    for index in range(len(list_i)):
        matrix_A = np.delete(matrix_A, list_i[index] - 1, 0)
        Jb = np.delete(Jb, list_k[index])

    return matrix_A, Jb


def main_phase_simplex_method(matrix_A, x, Jb, c):
    Jb[0] = 1
    x[3] = 0
    x[4] = 0


def get_transposed_matrix(matrix):
    return [list(elem) for elem in zip(*matrix)]


def get_basis_matrix(transposed_matrix, Jb):
    transposed_basis_matrix = [transposed_matrix[index - 1] for index in Jb]
    return get_transposed_matrix(transposed_basis_matrix)


if __name__ == '__main__':
    initial_phase_simplex_method(m, n, a, b, c)
