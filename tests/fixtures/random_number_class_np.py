import numpy as np
import unittest


class Tests(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.random_number = np.random.rand()

    def test_random(self):
        self.assertEqual(self.random_number, 0.417022004702574)


class TestsAgain(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.random_number = np.random.rand()

    def test_random_again(self):
        self.assertEqual(self.random_number, 0.417022004702574)
