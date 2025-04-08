import unittest
import numpy as np
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

#from solutions.electric_field_solution import calculate_potential, calculate_electric_field
from src.electric_field import calculate_potential, calculate_electric_field

class TestElectricField(unittest.TestCase):
    def setUp(self):
        self.spacing = 0.01
        x = np.linspace(-0.1, 0.1, 10)
        y = np.linspace(-0.1, 0.1, 10)
        self.X, self.Y = np.meshgrid(x, y)

    def test_potential_shape(self):
        V = calculate_potential(self.X, self.Y)
        self.assertEqual(V.shape, self.X.shape, "电势数组形状错误")

    def test_electric_field_shape(self):
        V = calculate_potential(self.X, self.Y)
        Ex, Ey = calculate_electric_field(V, self.spacing)
        self.assertEqual(Ex.shape, self.X.shape, "电场Ex数组形状错误")
        self.assertEqual(Ey.shape, self.Y.shape, "电场Ey数组形状错误")

    def test_potential_not_nan(self):
        V = calculate_potential(self.X, self.Y)
        self.assertFalse(np.isnan(V).any(), "电势计算结果包含NaN")

if __name__ == "__main__":
    unittest.main()