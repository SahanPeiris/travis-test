import unittest
from factorial import fact

class TestFactorial(unittest.TestCase):
    """
    Our basic test class
    """

    def test_fact(self):
        """
        The actual test.
        Any method which starts with ``test_`` will considered as a test case.
        """
        res = fact(5)
        self.assertEqual(res, 120)

    def test_will_fail(self):
        """
        A test put in place for the sharing
        """
        self.assertEqual(1, 2)


if __name__ == '__main__':
    unittest.main()
