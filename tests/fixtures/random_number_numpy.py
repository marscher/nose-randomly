import numpy as np
import unittest


class Tests(unittest.TestCase):

    def test_random(self):
        self.assertEqual(np.random.rand(), 0.417022004702574)
