import numpy as np


def double_simplex_method(matrix_A, b, c, Jb):
    n = len(c)
    basis_matrix = matrix_A[:, Jb]
    inverse_basis_matrix = np.linalg.inv(basis_matrix)
    c_basis = [c[i] for i in Jb]
    double_optimal_plan = (c_basis * inverse_basis_matrix).transpose()

    while True:
        pseudo_plan_basis = inverse_basis_matrix * b
        pseudo_plan = [0 if index not in Jb else pseudo_plan_basis[Jb.index(index)].item(0) for index in range(n)]

        negative_elements_indexes = get_negative_elements_indexes(pseudo_plan)

        if len(negative_elements_indexes) == 0:
            break

        j_s = negative_elements_indexes[0]
        delta_y = inverse_basis_matrix[Jb.index(j_s)]

        mu = get_mu_list(Jb, n, delta_y, matrix_A)
        if not have_solution(mu):
            print('No solution')
            return
        negative_mu = [(index, value) for index, value in enumerate(mu) if value < 0]

        j0, sigma0 = get_min_sigma_with_index(c, matrix_A, negative_mu, double_optimal_plan)
        double_optimal_plan = double_optimal_plan + sigma0.item(0) * delta_y.transpose()

        Jb[Jb.index(j_s)] = j0

        index = Jb.index(j0)
        inverse_basis_matrix = get_reverse_matrix(basis_matrix, inverse_basis_matrix, matrix_A[:, j0], index)
        basis_matrix[:, index] = matrix_A[:, j0]

    return pseudo_plan, Jb


def get_negative_elements_indexes(elements_list):
    return [index for index, value in enumerate(elements_list) if value < 0]


def get_mu_list(Jb, n, delta_y, matrix_A):
    return [delta_y * matrix_A[:, index] for index in range(n) if index not in Jb]


def have_solution(mu):
    for elem in mu:
        if elem < 0:
            return True
    return False


def get_min_sigma_with_index(c, A, mu, double_optimal_plan):
    sigmas = {index: (c[index] - A[:, index].transpose() * double_optimal_plan) / mu_value for index, mu_value in
              mu}
    min_sigma_index = min(sigmas, key=sigmas.get)
    return min_sigma_index, sigmas.get(min_sigma_index)


def get_reverse_matrix(source_matrix, source_reverse_matrix, vector, i):
    l = source_reverse_matrix * vector
    if l[i] == 0:
        return None

    li = l.item(i)
    l[i] = -1
    l_cap = -1 / li * l

    e = np.identity(len(source_matrix))
    e[:, i] = np.transpose(l_cap)
    reverse_matrix = e * source_reverse_matrix

    return reverse_matrix


def check_if_reverse_matrix_is_correct(source_matrix, reverse_matrix, vector, i):
    source_changed = source_matrix.copy()
    source_changed[:, i] = vector
    e = reverse_matrix.dot(source_changed)


if __name__ == '__main__':
    a_matrix = np.matrix([[1, -5, 1, 0],
                         [-3, 1, 0, 1]])
    b = np.matrix([[-10, -12]])
    c = [0, -6, 1, 0]
    initial_j_b = [2, 3]

    optimal_plan, j_b = double_simplex_method(a_matrix, b.transpose(), c, initial_j_b)
    print("Optimal plan: {}".format(optimal_plan))
    print("Basis indexes: {}".format(j_b))