import numpy as np

matrix_A = [[-1, 1, 1, 0, 0],
            [1, 0, 0, 1, 0],
            [0, 1, 0, 0, 1],
            ]

b = np.array([1, 3, 2])

x = np.array([0, 0, 1, 3, 2])

Jb = np.array([3, 4, 5])

c = np.array([1, 1, 0, 0, 0])


def main_phase_simplex_method(matrix_A, b, x, Jb, c):
    transposed_matrix_a = np.array(get_transposed_matrix(matrix_A))
    basis_matrix = get_basis_matrix(transposed_matrix_a, Jb)
    inverse_basis_matrix = np.linalg.inv(np.array(basis_matrix))
    potential_vector = get_potential_vector(inverse_basis_matrix, c, Jb)
    delta = get_delta(potential_vector, matrix_A, c)

    if not have_solution(delta):
        print('Unbounded')
        return
    print('Bounded')

    j0 = get_index_of_first_negative_element(delta)
    z = inverse_basis_matrix @ transposed_matrix_a[j0]
    return z


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


def have_solution(delta):
    for elem in delta:
        if elem < 0:
            return True
    return False


def get_index_of_first_negative_element(list):
    return next(index for index, value in enumerate(list) if value < 0)


print(main_phase_simplex_method(matrix_A, b, x, Jb, c))
