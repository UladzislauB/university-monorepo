import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve
import statsmodels.api as stm


class Solution:
    def __init__(self, alpha, N, autocorrelation):
        self.alpha = alpha
        self.N = N
        self.autocorrelation = autocorrelation

    @staticmethod
    def __generate_x_vector(n):
        return np.random.normal(0, 1 / 3, n)

    def __equations(self, c):
        R = self.__get_R_vector()
        a = np.array([[c[j] for j in range(k, self.N)] + [0] * k for k in range(self.N)])
        b = np.array([c[j] for j in range(self.N)])
        rez = np.dot(a, b)
        return [elem - R[i] for i, elem in enumerate(rez)]

    def __get_R_vector(self):
        return [autocorrelation(self.alpha, 0.4 * i) for i in range(0, self.N)]

    def __get_weighted_coefficients(self):
        return fsolve(self.__equations, [1] * self.N)

    def __get_random_process(self, n):
        x_vector = self.__class__.__generate_x_vector(n)
        c_vector = self.__get_weighted_coefficients()
        print(c_vector)
        return [sum([c_vector[k] * x_vector[i - k] for k in range(self.N)]) for i in range(self.N - 1, n)]

    @staticmethod
    def __get_expected_value(vector):
        return sum(vector) / len(vector)

    @staticmethod
    def __get_dispersion(vector, exp_value):
        return sum([(el - exp_value) ** 2 for el in vector]) / len(vector)

    def solve(self, n):
        random_process_vector = self.__get_random_process(n)
        print(random_process_vector)

        exp_val = self.__get_expected_value(random_process_vector)
        print('Expected value for random process:', exp_val)
        dispersion = self.__get_dispersion(random_process_vector, exp_val)
        print('Dispersion for random process:', dispersion)

        plt.plot(random_process_vector)
        plt.show()

        stm.graphics.tsa.plot_acf(random_process_vector, lags=(n - self.N))
        plt.show()


if __name__ == '__main__':
    autocorrelation = lambda alpha, tau: np.exp(- alpha * abs(tau)) * (1 - alpha * abs(tau))
    N = 13
    solution = Solution(1, N, autocorrelation)
    solution.solve(1000)
