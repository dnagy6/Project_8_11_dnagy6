"""
Module: tests.test_lifting
Purpose: Checks math logic and functionality for the LiftingCalculator class.
"""

import unittest
from calculators.lifting import LiftingCalculator

class TestLiftingCalculator(unittest.TestCase):
    """Test suite for the barbell math and periodization logic."""

    def setUp(self):
        # This runs automatically before every test to give us a fresh calculator object
        self.calc = LiftingCalculator()

    def test_estimate_1rm_epley(self):
        """Checks if the Epley formula calculates correctly."""
        # Math logic: 225 lbs for 5 reps = 225 * (1 + 5/30) = 262.5
        estimated_max = self.calc.estimate_1rm(225, 5)
        self.assertEqual(estimated_max, 262.5)

    def test_estimate_1rm_single(self):
        """Checks if a true 1RM input bypasses the formula."""
        true_max = self.calc.estimate_1rm(315, 1)
        self.assertEqual(true_max, 315.0)

    def test_calculate_block(self):
        """Checks if the 4-week percentages calculate and round correctly."""
        # Using 100 lbs makes the percentage math obvious (65% of 100 = 65.0)
        training_block = self.calc.calculate_block(100)
        
        self.assertEqual(training_block["Week 1 (65%)"]["weight"], 65.0)
        self.assertEqual(training_block["Week 2 (75%)"]["weight"], 75.0)
        self.assertEqual(training_block["Week 3 (85%)"]["weight"], 85.0)
        self.assertEqual(training_block["Week 4 (Deload)"]["weight"], 50.0)

if __name__ == '__main__':
    unittest.main()