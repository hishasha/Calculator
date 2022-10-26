import time
import unittest

from mod2 import _mult
from constants import TEST_LIST


"""
Значения времени, которые получались на данном файле. Возьмем в качестве верхней границы 0.02
0.005293369293212891
0.007315635681152344
0.0010018348693847656
0.0027534961700439453
0.004830837249755859
0.0045588016510009766
0.019502878189086914
"""
TIME_BOUNDARY = 0.02


class PerformanceTest(unittest.TestCase):
    def test_mult(self):
        time_before = time.time()
        _mult(TEST_LIST)
        time_after = time.time()
        self.assertLess(time_after - time_before, TIME_BOUNDARY)


if __name__ == '__main__':
    unittest.main()
