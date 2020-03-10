import numpy


class OptimizedSolution:

    def __init__(self, matrix, inverse_matrix, column, x):
        self.matrix = matrix
        self.inverse_matrix = inverse_matrix
        self.column = column - 1
        self.x = x

    def answer(self):
        l = self.inverse_matrix @ self.x

        if l[self.column] == 0:
            return None

        l_tilda = numpy.copy(l)
        l_tilda[self.column] = -1

        l_upper = -1. / l[self.column] * l_tilda
        q = numpy.eye(len(self.matrix))
        q[:, self.column] = l_upper[:, 0]

        answer = q @ self.inverse_matrix

        return answer


if __name__ == '__main__':
    matrix = numpy.array([[1., 0., 5.],
                          [2., 1., 6.],
                          [3., 4., 0.]])

    inverse_matrix = numpy.array([[-24., 20., -5.],
                                  [18., -15., 4.],
                                  [5., -4., 1.]])

    column = 2

    x = numpy.array([[2.], [2.], [2.]])
    solution = OptimizedSolution(matrix, inverse_matrix, column, x)

    answer = solution.answer()

    if answer is not None:
        print(answer)
        new_matrix = numpy.copy(matrix)
        new_matrix[:, column - 1] = x[:, 0]
        print(new_matrix @ answer)
    else:
        print('The matrix is not invertible')
