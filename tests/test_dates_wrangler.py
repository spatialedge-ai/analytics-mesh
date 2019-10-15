import unittest
import mesh.dates.wrangler
from datetime import datetime


class TestDateFormatter(unittest.TestCase):

    def testYYYYMM(self):
        self.assertEqual(datetime(2020, 1, 1), mesh.dates.wrangler.yyyymmdd_to_datetime('202001', 1))

    def testYYYYMMDD(self):
        self.assertEqual(datetime(2020, 1, 20), mesh.dates.wrangler.yyyymmdd_to_datetime('20200120', 1))
        self.assertEqual(datetime(2020, 1, 20), mesh.dates.wrangler.yyyymmdd_to_datetime('20200120'))

    def testNegative(self):
        with self.assertRaises(ValueError):
            mesh.dates.wrangler.yyyymmdd_to_datetime('2010')
        with self.assertRaises(ValueError):
            self.assertEqual(datetime(2020, 1, 1), mesh.dates.wrangler.yyyymmdd_to_datetime('202001'))

