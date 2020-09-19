from typing import List, Tuple
import matplotlib.pyplot as plt


class Solution:
    def get_mid_square_random_values(self, a0: int, n: int) -> List[float]:
        seq = []
        temp = ''.join([val for val in str(a0 ** 2)])
        j = 1
        while j < 5 and int(temp[j:j + 4]) < 1000:
            j += 1
        a1 = int(temp[j:j + 4])
        if a1 < 1000:
            print('Error. Bad a0. Choose another value')
            return []
        seq.append(a1)

        for i in range(1, n + 1):
            temp = ''.join([val for val in str(seq[i - 1] ** 2)])
            j = 1
            while j < 5 and int(temp[j:j + 4]) < 1000:
                j += 1
            new_a = int(temp[j:j + 4])
            if new_a < 1000:
                print('Error. Algorithm was interrupted. Choose another start value')
                return seq
            seq.append(new_a)
        return [elem / 9999 for elem in seq]

    def get_multiplicative_congruential_random_values(self, m: int, k: int, a0: int, n: int) -> List[float]:
        seq = []
        a1 = ((k * a0) % m)
        if a1 == 0:
            print('Error. Period became 0. Bad combination of start values')
            return []
        seq.append(a1)
        for i in range(1, n + 1):
            new_a = ((k * seq[i - 1]) % m)
            if new_a == 0:
                print('Error. Period became 0. Bad combination of start values')
                return seq
            seq.append(new_a)
        return [val / m for val in seq]

    def uniformity_test(self, arr100: List[float], arr10000: List[float], k: int) -> Tuple[
        float, float, List[float], List[float]]:
        n100 = [0] * (k + 1)
        for elem in arr100:
            n100[int(elem * k)] += 1
        n100[k - 1] += n100.pop()
        p100 = [elem / 100 for elem in n100]

        expected_value = 0
        dispersion = 0

        n10000 = [0] * (k + 1)
        for elem in arr10000:
            n10000[int(elem * k)] += 1
            expected_value += elem
        n10000[k - 1] += n10000.pop()
        p10000 = [elem / 10000 for elem in n10000]

        expected_value /= 10000
        expected_value_pow_2 = expected_value ** 2
        for elem in arr10000:
            dispersion += elem ** 2 - expected_value_pow_2
        dispersion /= 10000

        return expected_value, dispersion, p100, p10000

    def draw_plots(self, p100: List[float], p10000: List[float]) -> None:
        plt.plot([0.1 * i for i in range(10)], p100, color='red')
        plt.plot([0.1 * i for i in range(10)], p10000)
        plt.show()

    def independence_test(self, m_x: float, d_x: float, m_y: float, d_y: float, m_xy: float):
        return (m_xy - m_x * m_y) / ((d_x * d_y) ** (1 / 2))

    def get_expected_value_and_dispersion(self, arr: List[float]):
        expected_value = 0
        for elem in arr:
            expected_value += elem
        expected_value /= len(arr)
        ex_pow_2 = expected_value ** 2

        dispersion = 0
        for elem in arr:
            dispersion += elem ** elem - ex_pow_2
        dispersion /= len(arr)

        return expected_value, dispersion


if __name__ == '__main__':
    solution = Solution()

    arr_square_100 = solution.get_mid_square_random_values(1234, 100)
    arr_square_10000 = solution.get_mid_square_random_values(4823, 10000)

    expected_value, dispersion, p100, p10000 = solution.uniformity_test(arr_square_100, arr_square_10000, 10)
    solution.draw_plots(p100, p10000)
    print('expected_value', expected_value, 'dispersion', dispersion)
    new_arr = solution.get_mid_square_random_values(3422, 10000)
    m_y, d_y = solution.get_expected_value_and_dispersion(new_arr)
    m_xy, _ = solution.get_expected_value_and_dispersion([arr_square_10000[i] * new_arr[i] for i in range(10000)])
    print('Coefficient  correlation', solution.independence_test(expected_value, dispersion, m_y, d_y, m_xy))


    arr_mul_100 = solution.get_multiplicative_congruential_random_values(42949, 72315, 124, 100)
    arr_mul_10000 = solution.get_multiplicative_congruential_random_values(42949, 72315, 124, 10000)

    expected_value, dispersion, p100, p10000 = solution.uniformity_test(arr_mul_100, arr_mul_10000, 10)
    solution.draw_plots(p100, p10000)
    print('expected_value', expected_value, 'dispersion', dispersion)
    new_arr = solution.get_multiplicative_congruential_random_values(4294913, 36315, 124, 10000)
    m_y, d_y = solution.get_expected_value_and_dispersion(new_arr)
    m_xy, _ = solution.get_expected_value_and_dispersion([arr_square_10000[i] * new_arr[i] for i in range(10000)])
    print('Coefficient  correlation', solution.independence_test(expected_value, dispersion, m_y, d_y, m_xy))
