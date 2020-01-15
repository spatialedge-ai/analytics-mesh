import pandas as pd
from abc import ABCMeta


class Validator(metaclass=ABCMeta):
    pass  # pragma: no cover


class Pandas(Validator):

    def __init__(self, series: pd.Series):
        self.series = series

    def range(self, min, max):
        """
        validate a series against the range provided
        :param min: the lower bound of an interval
        :param max: the upper bound of an interval
        :return: this validator
        """
        smin = self.series.min()
        smax = self.series.max()
        if smin < min or smax > max:
            raise ValueError('range [{}, {}] not within [{}, {}]'.format(smin, smax, min, max))
        return self
