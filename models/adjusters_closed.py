import numpy as np


class ModelAdjustersClosed:
    def __init__(self, broken_t, handling_t, channels, adjusters):
        self.broken_i = 1 / broken_t
        self.handling_i = 1 / handling_t
        self._channels = channels
        self._adjusters = adjusters

    @property
    def adjusters(self):
        return self._adjusters

    @adjusters.setter
    def adjusters(self, value):
        if value <= 0:
            raise ValueError("number of adjusters must be higher or equal to 1")

        self._adjusters = value

    def get_pi_arg(self, index):
        if index <= 0:
            raise ValueError("index must be more than '0'")

        if index <= self._adjusters:
            braces = np.power(self.broken_i / self.handling_i, index)
            result = np.math.factorial(self._channels) / (
                    np.math.factorial(self._channels - index) * np.math.factorial(index)) * braces
        else:
            index -= self._adjusters
            braces = np.power(self.broken_i / (self.handling_i * self._adjusters), index)
            result = np.math.factorial(self._channels - self._adjusters) / (
                np.math.factorial(self._channels - self._adjusters - index)) * braces * self.get_pi_arg(self._adjusters)

        return result

    def get_p0(self):
        denom = np.sum([self.get_pi_arg(i) for i in range(1, self._channels + 1)]) + 1
        return 1 / denom

    def broken_channels(self):
        return self.get_p0() * np.sum([i * self.get_pi_arg(i) for i in range(1, self._channels + 1)])

    def waited_channels(self):
        return self.get_p0() * np.sum(
            [i * self.get_pi_arg(self._adjusters + i) for i in range(1, self._channels - self._adjusters + 1)])

    def waiting_probability(self):
        return self.get_p0() * np.sum(
            [self.get_pi_arg(self._adjusters + i) for i in range(1, self._channels - self._adjusters + 1)])

    def busy_adjusters(self):
        summary = np.sum([i * self.get_pi_arg(i) for i in range(1, self._adjusters + 1)])
        summary += self._adjusters * np.sum(
            [self.get_pi_arg(self._adjusters + i) for i in range(1, self._channels - self._adjusters + 1)])
        return self.get_p0() * summary

    def busy_adjucters_coef(self):
        return self.busy_adjusters() / self._adjusters
