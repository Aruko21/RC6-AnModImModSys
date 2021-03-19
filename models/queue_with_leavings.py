from .without_queue import ModelWithoutQueue

import numpy as np


class ModelQueueLeavings(ModelWithoutQueue):
    def __init__(self, client_t, handling_t, leaving_t, channels, eps=1e-9):
        self.leaving_i = 1 / leaving_t
        self.eps = eps
        super().__init__(client_t, handling_t, channels)

    def get_pi_arg(self, index):
        if index <= 0:
            raise ValueError("index must be more than '0'")

        if index <= self._channels:
            result = np.power(self.client_i, index) / (np.math.factorial(index) * np.power(self.handling_i, index))
        else:
            result = np.power(self.client_i, index - self._channels) * self.get_pi_arg(self._channels)
            result /= np.prod(
                [(self._channels * self.handling_i + i * self.leaving_i) for i in range(1, index - self._channels + 1)])
        return result

    def get_infinite_series(self, func_series, attempts=100):
        summ_i = None
        is_converge = False

        for i in range(attempts):
            next_value = func_series(i)
            if summ_i:
                if np.fabs(next_value) < self.eps:
                    summ_i += next_value
                    is_converge = True
                    break
            else:
                summ_i = next_value

        if not is_converge:
            return ValueError("Series is not converge")
        else:
            return summ_i

    def get_p0(self):
        denom = np.sum([self.get_pi_arg(i) for i in range(1, self._channels + 1)]) + 1
        denom += self.get_pi_arg(self._channels) * self.get_infinite_series(
            lambda k: np.power(self.client_i, k) / (self._channels * self.handling_i + k * self.leaving_i),
            attempts=100
        )

        return 1 / denom

    def busy_operators(self):
        summary = np.sum([i * self.get_pi_arg(i) for i in range(1, self._channels + 1)])
        summary += self.channels * self.get_pi_arg(self._channels) * self.get_infinite_series(
            lambda k: np.power(self.client_i, k) / (self._channels * self.handling_i + k * self.leaving_i),
            attempts=100
        )
        return self.get_p0() * summary

    def queue_prob(self):
        return self.get_p0() * self.get_pi_arg(self._channels) * self.get_infinite_series(
            lambda k: np.power(self.client_i, k) / (self._channels * self.handling_i + k * self.leaving_i),
            attempts=100
        )

    def queue_length_expect(self):
        return self.get_p0() * self.get_pi_arg(self._channels) * self.get_infinite_series(
            lambda k: k * np.power(self.client_i, k) / (self._channels * self.handling_i + k * self.leaving_i),
            attempts=100
        )
