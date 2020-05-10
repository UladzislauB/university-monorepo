import numpy as np
import math


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

    print('Bounded')
    print(*["{0:0.10f}".format(i) for i in x])
    print('\nJb =', Jb)
    print('A =', matrix_A)


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
    transposed_matrix_a = np.array(get_transposed_matrix(matrix_A))
    basis_matrix = np.array(get_basis_matrix(transposed_matrix_a, Jb))
    inverse_basis_matrix = np.linalg.inv(np.array(basis_matrix))
    column = 0
    vector = []

    is_first_iteration = True

    while True:
        if not is_first_iteration:
            inverse_basis_matrix = get_optimized_inverse_matrix(basis_matrix, inverse_basis_matrix, column, vector)
            basis_matrix = np.array(get_basis_matrix(transposed_matrix_a, Jb))
        else:
            is_first_iteration = False

        potential_vector = get_potential_vector(inverse_basis_matrix, c, Jb)
        delta = get_delta(potential_vector, matrix_A, c)

        # Решение оптимально, выход из цикла
        if is_optimal_solution(delta, Jb):
            return

        j0 = get_index_of_first_negative_element(delta)
        z = inverse_basis_matrix @ transposed_matrix_a[j0]
        theta = get_vector_theta(z, x, Jb)

        if not have_solution(theta):
            return

        index_min, theta0 = min(enumerate(theta)
                                , key=lambda pair: pair[1])
        Jb[index_min] = j0 + 1
        # Defining of vector and column number for optimized inversion of matrix
        column = index_min
        vector = matrix_A[:, j0]
        x = get_new_plan_x(x, theta0, Jb, j0, z)


def get_transposed_matrix(matrix):
    return [list(elem) for elem in zip(*matrix)]


def get_basis_matrix(transposed_matrix, Jb):
    transposed_basis_matrix = [transposed_matrix[index - 1] for index in Jb]
    return get_transposed_matrix(transposed_basis_matrix)


def get_potential_vector(inverse_basis_matrix, c, Jb):
    basis_c = [c[index - 1] for index in Jb]
    return basis_c @ inverse_basis_matrix


def get_delta(potential_vector, matrix_A, c):
    return potential_vector @ matrix_A - c


def is_optimal_solution(delta, Jb):
    for index, value in enumerate(delta):
        if index + 1 not in Jb and value < 0:
            return False
    return True


def get_index_of_first_negative_element(list):
    return next(index for index, value in enumerate(list) if value < 0)


def get_vector_theta(z, x, Jb):
    return [x[Jb[index] - 1] / value if value > 0 else math.inf for index, value in enumerate(z)]


def have_solution(theta):
    for elem in theta:
        if elem is not math.inf:
            return True
    return False


def get_new_plan_x(x, theta0, Jb, j0, z):
    new_plan_x = [0] * len(x)
    for index, value in enumerate(Jb):
        new_plan_x[value - 1] = x[value - 1] - theta0 * z[index]
    new_plan_x[j0] = theta0
    return new_plan_x


def get_optimized_inverse_matrix(matrix, inverse_matrix, column, vector):
    l = inverse_matrix @ vector

    if l[column] == 0:
        return None

    l_tilda = np.copy(l)
    l_tilda[column] = -1

    l_upper = -1. / l[column] * l_tilda
    q = np.eye(len(matrix))
    q[:, column] = l_upper

    answer = q @ inverse_matrix

    return answer


def get_list_int_from_string(string):
    return [int(elem) for elem in string.split()]


if __name__ == '__main__':
    matrix_A = []
    b = []
    c = []

    with open('input.txt', 'r') as f:
        m, n = [int(elem) for elem in f.readline().split()]
        for _ in range(m):
            matrix_A.append(get_list_int_from_string(f.readline()))
        b = np.array(get_list_int_from_string(f.readline()))
        c = np.array(get_list_int_from_string(f.readline()))
    initial_phase_simplex_method(m, n, matrix_A, b, c)
