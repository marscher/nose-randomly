import numpy as np
import unittest


class Tests(unittest.TestCase):
    def test_not_reseeded_to_100(self):
        numbers = np.random.random(100)

        # Now reseed with 100 to find what the first 100 numbers *would* be
        np.random.seed(100)
        numbers_seed_100 = np.random.random(100)
        self.assertFalse(np.allclose(numbers, numbers_seed_100))
