import unittest

class TestExamples(unittest.TestCase):

    def test_equal(self):
        self.assertEqual(10, 10)

    def test_not_equal(self):
        self.assertNotEqual(10, 20)

    def test_true(self):
        self.assertTrue(5 > 2)

    def test_false(self):
        self.assertFalse(5 < 2)

    def test_membership(self):
        self.assertIn("Python", ["Java", "Python"])

if __name__ == "__main__":
    unittest.main()