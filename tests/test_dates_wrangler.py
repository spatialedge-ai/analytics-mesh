import unittest
import mesh.dates.wrangler
from datetime import datetime


class TestDateFormatter(unittest.TestCase):

    def testYYYYMM(self):
        self.assertEqual(datetime(2020, 1, 1), mesh.dates.wrangler.date_formatter('202001', 1))

    def testYYYYMMDD(self):
        self.assertEqual(datetime(2020, 1, 20), mesh.dates.wrangler.date_formatter('20200120', 1))