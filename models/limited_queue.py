from .without_queue import ModelWithoutQueue

import numpy as np


class ModelLimitedQueue(ModelWithoutQueue):
    def __init__(self, client_t, handling_t, channels, q_len):
        self._q_len = q_len
        super().__init__(client_t, handling_t, channels)

    @property
    def q_len(self):
        return self._q_len

    @q_len.setter
    def q_len(self, value):
        if value <= 0:
            raise ValueError("queue length must be higher or equal to 1")

        self._q_len = value

    def get_pi_arg(self, index):
        if index <= 0:
            raise ValueError("index must be more than '0'")

        if index <= self._channels:
            result = np.power(self.client_i, index) / (np.math.factorial(index) * np.power(self.handling_i, index))
        else:
            coef = self.client_i / (self._channels * self.handling_i)
            result = np.power(coef, index - self._channels) * self.get_pi_arg(self._channels)

        return result

    def get_p0(self):
        denom = np.sum([self.get_pi_arg(i) for i in range(1, self._channels + self._q_len + 1)]) + 1
        return 1 / denom

    def denial_prob(self):
        return self.get_p0() * self.get_pi_arg(self._channels + self._q_len)

    def busy_operators(self):
        summary = np.sum([i * self.get_pi_arg(i) for i in range(1, self._channels + 1)])
        summary += np.sum([self._channels * self.get_pi_arg(self._channels + j) for j in range(1, self._q_len + 1)])
        return self.get_p0() * summary

    def queue_prob(self):
        summary = np.sum([self.get_pi_arg(self._channels + j) for j in range(1, self._q_len + 1)])
        return self.get_p0() * summary

    def queue_length_expect(self):
        summary = np.sum([i * self.get_pi_arg(self._channels + i) for i in range(1, self._q_len + 1)])
        return self.get_p0() * summary

    def queue_busy_coef(self):
        return self.queue_length_expect() / self._q_len
