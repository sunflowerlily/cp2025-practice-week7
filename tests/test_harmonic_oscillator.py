import unittest
import numpy as np
import sympy as sp
import sys
import os

# Add the parent directory to the Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from solutions.harmonic_oscillator_solution import symbolic_solution, numeric_solution



class TestHarmonicOscillator(unittest.TestCase):
    def setUp(self):
        self.m = 1.0
        self.k = 1.0
        self.x0 = 1.0
        self.v0 = 0.0
        self.t = np.linspace(0, 10, 100)

    def test_symbolic_solution(self):
        sol = symbolic_solution(self.m, self.k, self.x0, self.v0)
        self.assertTrue(isinstance(sol, sp.Eq), "Symbolic solution should be an equation type (sympy.Eq).")

    def test_numeric_solution_shape(self):
        numeric_sol = numeric_solution(self.m, self.k, self.x0, self.v0, self.t)
        self.assertEqual(numeric_sol.shape, self.t.shape, "Numeric solution should have the same shape as time array.")

    def test_numeric_solution_initial_conditions(self):
        numeric_sol = numeric_solution(self.m, self.k, self.x0, self.v0, self.t)
        self.assertAlmostEqual(numeric_sol[0], self.x0, places=5, msg="Numeric solution initial value mismatch.")

if __name__ == '__main__':
    unittest.main()