import unittest
from mesh.dataframes.validators import Pandas
import pandas as pd


class TestPanda(unittest.TestCase):

    def setUp(self):
        self.series = pd.Series([0, 1, 2, 3, 4])

    def test_range(self):
        validator = Pandas(self.series)
        validator.range(0, 4)

    def test_range_fail(self):
        validator = Pandas(self.series)
        # upper
        with self.assertRaises(ValueError):
            validator.range(0, 3)
        # lower
        with self.assertRaises(ValueError):
            validator.range(1, 5)
        # both
        with self.assertRaises(ValueError):
            validator.range(2, 3)



