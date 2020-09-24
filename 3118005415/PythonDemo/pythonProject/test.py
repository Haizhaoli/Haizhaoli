import unittest
from main import get_cos, sample_data, compare_data


class MyTestCase(unittest.TestCase):
    def test_something(self):
        self.assertEqual(get_cos(sample_data, compare_data), False)


if __name__ == '__main__':
    unittest.main()
