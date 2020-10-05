from random import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable


class Solution:
    x_vector = []
    y_vector = []

    def __init__(self, f_xy, f_x, a, b, w_x, n):
        self.f_xy = f_xy
        self.f_x = f_x
        self.a = a
        self.b = b
        self.w_x = w_x
        self.n = n

    def count_x_vector(self):
        while len(self.x_vector) < self.n:
            r1, r2 = random(), random()
            x1, x2 = self.a + (self.b - self.a) * r1, self.w_x * r2
            if x2 < self.f_x(x1):
                self.x_vector.append(x1)

    def count_y_vector(self):
        j = 0
        while j < self.n:
            w_y = self.f_xy(self.x_vector[j], 1) / self.f_x(self.x_vector[j])
            while True:
                r1, r2 = random(), random()
                y1, y2 = self.a + (self.b - self.a) * r1, w_y * r2
                if y2 < self.f_xy(self.x_vector[j], y1) / self.f_x(self.x_vector[j]):
                    self.y_vector.append(y1)
                    j += 1
                    break

    def get_intervals(self, x_vector, y_vector, intervals_count):
        intervals_x, intervals_y = [0] * intervals_count, [0] * intervals_count
        for i in range(self.n):
            intervals_x[int(x_vector[i] * intervals_count)] += 1
            intervals_y[int(y_vector[i] * intervals_count)] += 1
        p_x_interval, p_y_interval = [elem / self.n for elem in intervals_x], [elem / self.n for elem in intervals_y]
        return p_x_interval, p_y_interval

    def draw_histogram(self, p_x_interval, p_y_interval, intervals_count):
        plt.plot(p_x_interval, color='blue', drawstyle='steps-pre')
        plt.show()
        plt.plot(p_y_interval, color='red', drawstyle='steps-pre')
        plt.show()

    def get_expected_value_and_dispersion(self, vector):
        exp_value = 0
        for num in vector:
            exp_value += num
        exp_value /= self.n

        exp_pow_2 = exp_value ** 2
        dispersion = 0
        for num in vector:
            dispersion += num ** 2 - exp_pow_2
        dispersion /= self.n

        return exp_value, dispersion

    def get_exp_value_xy(self, vector_x, vector_y):
        s = 0
        for j in range(self.n):
            s += vector_x[j] * vector_y[j]
        s /= self.n
        return s

    def get_coef_correlation(self, exp_val_x, disp_x, exp_val_y, disp_y, m_xy):
        return (m_xy - exp_val_x * exp_val_y) / ((disp_x * disp_y) ** (1 / 2))

    def solve_task_1(self, count_intervals):
        self.count_x_vector()
        self.count_y_vector()
        intevals_x, intervals_y = self.get_intervals(self.x_vector, self.y_vector, count_intervals)
        self.draw_histogram(intevals_x, intervals_y, count_intervals)

        # Plot for probability density from y
        test = []
        test_x = []
        for _ in range(self.n):
            y = random()
            test_x.append(y)
            test.append(2 * (1 + y) / 3)
        plt.plot(test_x, test, color='green')
        plt.show()

        exp_value_x, dispersion_x = self.get_expected_value_and_dispersion(self.x_vector)
        print(f'Expected value for x: {exp_value_x}, dispersion for x: {dispersion_x}')
        exp_value_y, dispersion_y = self.get_expected_value_and_dispersion(self.y_vector)
        print(f'Expected value for y: {exp_value_y}, dispersion for y: {dispersion_y}')
        m_xy = self.get_exp_value_xy(self.x_vector, self.y_vector)
        coef_correlation = self.get_coef_correlation(exp_value_x, dispersion_x, exp_value_y, dispersion_y, m_xy)
        print('Coefficient of correlation:', coef_correlation)

    p_matrix = []
    component_a = []
    component_b = []
    p_vector_x = []
    p_matrix_y = []
    distribution_function_x = [0]
    distribution_function_y = []
    discrete_x_vector = []
    discrete_y_vector = []

    def generate_p_matrix(self, n, m):
        base = [[int(random() * 1000) for _ in range(n)] for _ in range(m)]
        total_sum = sum([sum(row) for row in base])
        self.component_a = [int(random() * 1000) for _ in range(m)]
        self.component_b = [int(random() * 1000) for _ in range(n)]
        x = PrettyTable()

        print('Possibility matrix')
        x.field_names = ['A\B'] + ['B' + str(i) + ': ' + str(elem) for i, elem in enumerate(self.component_b)]
        self.p_matrix = [[elem / total_sum for elem in row] for row in base]
        for index, row in enumerate(self.p_matrix):
            x.add_row([self.component_a[index]] + row)
        print(x)
        print('Sum of elements in possibility matrix=', sum([sum(row) for row in self.p_matrix]))

    def count_p_vectors_and_distribution_funcs(self):
        self.p_vector_x = [sum(row) for row in self.p_matrix]
        s = 0
        for p in self.p_vector_x:
            s += p
            self.distribution_function_x.append(s)
        print('Distribution function for X: ', self.distribution_function_x)
        self.p_matrix_y = [[p / self.p_vector_x[r_index] for p in row] for r_index, row in enumerate(self.p_matrix)]
        for row in self.p_matrix_y:
            s = 0
            list = [0]
            for p_y in row:
                s += p_y
                list.append(s)
            self.distribution_function_y.append(list)

        x = PrettyTable()
        x.field_names = ['Xi\Yj'] + [*range(len(self.component_b))] + ['>']
        for r_index, row in enumerate(self.distribution_function_y):
            x.add_row([self.component_a[r_index]] + row)
        print('Distribution function for Yj if Xi:')
        print(x)

    def generate_discrete_random_values(self):
        for _ in range(self.n):
            r = random()
            k = 0
            while self.distribution_function_x[k] < r:
                k += 1
            x = self.component_a[k - 1]
            r = random()
            t = 0
            while self.distribution_function_y[k - 1][t] < r:
                t += 1
            y = self.component_b[t - 1]
            self.discrete_x_vector.append(x)
            self.discrete_y_vector.append(y)

    def get_discrete_intervals(self):
        d1 = {key: 0 for key in self.component_a}
        d2 = {key: 0 for key in self.component_b}

        for i in range(self.n):
            d1[self.discrete_x_vector[i]] += 1
            d2[self.discrete_y_vector[i]] += 1

        return list(d1.values()), list(d2.values())

    def solve_task_2(self, n, m, intervals_count):
        self.generate_p_matrix(n, m)
        self.count_p_vectors_and_distribution_funcs()
        self.generate_discrete_random_values()

        intervals_x, intervals_y = self.get_discrete_intervals()
        p_intervals_x, p_intervals_y = [elem / self.n for elem in intervals_x], [elem / self.n for elem in intervals_y]
        plt.plot(self.component_a, p_intervals_x, 'ro', color='blue')
        plt.show()
        plt.plot(self.component_b, p_intervals_y, 'ro', color='red')
        plt.show()


if __name__ == '__main__':
    f_xy = lambda x, y: 2 * (x ** 2 + y / 3)
    f_x = lambda x: 2 * (x ** 2) + (1 / 3)
    a = 0
    b = 1
    w_x = 7 / 3
    solution = Solution(f_xy, f_x, a, b, w_x, 10000)
    solution.solve_task_1(20)
    n = 7
    m = 8
    solution.solve_task_2(n, m, 20)
