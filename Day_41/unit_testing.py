# 2. What is Unit Testing?
#   --Unit testing means testing small individual parts of a program, usually functions or methods.

import unittest

def add(a, b):
    return a + b


class TestAddition(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(10, 20), 30)


if __name__ == "__main__":
    unittest.main()