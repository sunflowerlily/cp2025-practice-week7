import unittest
import numpy as np
from solutions.two_dimensional_velocity_field import source_flow, vortex_flow

class TestFlowField(unittest.TestCase):
    def test_source_flow(self):
        X, Y = np.array([[1.0]]), np.array([[0.0]])
        u, v = source_flow(2*np.pi, X, Y)
        self.assertAlmostEqual(u[0,0], 1.0, places=5)
        self.assertAlmostEqual(v[0,0], 0.0, places=5)

    def test_vortex_flow(self):
        X, Y = np.array([[0.0]]), np.array([[1.0]])
        u, v = vortex_flow(2*np.pi, X, Y)
        self.assertAlmostEqual(u[0,0], -1.0, places=5)
        self.assertAlmostEqual(v[0,0], 0.0, places=5)

if __name__ == '__main__':
    unittest.main()