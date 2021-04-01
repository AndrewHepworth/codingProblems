from unittest import TestCase
from twoD_Array import hourglass_sum

arr = [[1, 1, 1, 0, 0, 0],
       [0, 1, 0, 0, 0, 0],
       [1, 1, 1, 0, 0, 0],
       [0, 0, 2, 4, 4, 0],
       [0, 0, 0, 2, 0, 0],
       [0, 0, 1, 2, 4, 0]]


class Test_hourglass(TestCase):
    def test_hourglass_sum(self):
        self.assertEqual(hourglass_sum(arr), 19)
