import numpy as np


class ModelWithoutQueue:
    def __init__(self, client_t, handling_t):
        self.client_i = 1 / client_t
        self.handling_i = 1 / handling_t

    def get_pi_arg(self, index):
        if index <= 0:
            raise ValueError("index must be more than '0'")

        return np.power(self.client_i, index) / (np.math.factorial(index) * np.power(self.handling_i, index))

    def get_p0(self, n):
        denom = np.sum([self.get_pi_arg(i) for i in range(1, n + 1)])
        return 1 / denom

    def denial_prob(self, n):
        return self.get_p0(n) * self.get_pi_arg(n)

    def busy_operators(self, n):
        summary = np.sum([i * self.get_pi_arg(i) for i in range(1, n + 1)])
        return self.get_p0(n) * summary

    def busy_coefficient(self, n):
        return self.busy_operators(n) / n
