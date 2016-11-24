import unittest

from play.prime import is_prime, next_prime


class MyTestCase(unittest.TestCase):

    def test_is_prime_for_first_prime(self):
        self.assertEqual(True, is_prime(2))

    def test_is_prime_for_large_prime(self):
        self.assertEqual(True, is_prime(67))

    def test_is_prime_for_negative(self):
        self.assertEqual(False, is_prime(-1))

    def test_is_prime_for_zero(self):
        self.assertEqual(False, is_prime(0))

    def test_is_prime_for_one(self):
        self.assertEqual(False, is_prime(1))

    def test_next_prime_for_large_prime(self):
        self.assertEqual(11, next_prime(9))

    def test_next_prime_for_prime_input(self):
        self.assertEqual(13, next_prime(11))

    def test_next_prime_for_negative_input(self):
        self.assertEqual(2, next_prime(-1))


if __name__ == '__main__':
    unittest.main()
