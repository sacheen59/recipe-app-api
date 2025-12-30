"""
Sample tests
"""


from django.test import SimpleTestCase

from .calc import add, subtract


class CalcTest(SimpleTestCase):
    """testing calc module"""

    def test_add_numbers(self):
        """Test adding numbers together."""
        res = add(5, 6)
        self.assertEqual(res, 11)

    def test_subtract_number(self):
        """Test subtracting two numbers."""
        res = subtract(15, 10)
        self.assertEqual(res, 5)
