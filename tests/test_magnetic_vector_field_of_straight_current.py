import unittest
import numpy as np
from main import wire_magnetic_field
from scipy.constants import mu_0

class TestMagneticField(unittest.TestCase):
    def test_wire_magnetic_field(self):
        I = 1
        X, Y = np.array([[1.0]]), np.array([[0.0]])
        Bx, By = wire_magnetic_field(I, X, Y)
        expected_B = mu_0 * I / (2 * np.pi * 1)
        self.assertAlmostEqual(Bx[0,0], 0.0, places=5)
        self.assertAlmostEqual(By[0,0], expected_B, places=5)

if __name__ == '__main__':
    unittest.main()