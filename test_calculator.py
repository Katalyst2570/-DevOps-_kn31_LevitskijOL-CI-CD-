import unittest
from calculator import add, subtract

class TestCalculator(unittest.TestCase):
    def test_add(self):
        """Перевіряє, чи працює функція додавання."""
        self.assertEqual(add(3, 4), 7)

    def test_subtract(self):
        """Перевіряє, чи працює функція віднімання."""
        self.assertEqual(subtract(5, 2), 3)

if __name__ == '__main__':
    unittest.main()

