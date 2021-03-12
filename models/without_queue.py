import numpy as np


class ModelWithoutQueue:
    def __init__(self, client_t, handling_t, channels):
        self.client_i = 1 / client_t
        self.handling_i = 1 / handling_t
        self._channels = channels

    @property
    def channels(self):
        return self._channels

    @channels.setter
    def channels(self, value):
        if value <= 0:
            raise ValueError("number of channels must be higher or equal to 1")

        self._channels = value

    def get_pi_arg(self, index):
        if index <= 0:
            raise ValueError("index must be more than '0'")
        return np.power(self.client_i, index) / (np.math.factorial(index) * np.power(self.handling_i, index))

    def get_p0(self):
        denom = np.sum([self.get_pi_arg(i) for i in range(1, self._channels + 1)]) + 1
        # print("without denom: ", 1 / denom)
        return 1 / denom

    def denial_prob(self):
        return self.get_p0() * self.get_pi_arg(self._channels)

    def busy_operators(self):
        summary = np.sum([i * self.get_pi_arg(i) for i in range(1, self._channels + 1)])
        return self.get_p0() * summary

    def busy_coefficient(self):
        return self.busy_operators() / self._channels
