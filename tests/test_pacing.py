"""
Module: tests.test_pacing
Purpose: Automated logic checks for the PacingCalculator engine.
"""

import unittest
from calculators.pacing import PacingCalculator

class TestPacingCalculator(unittest.TestCase):
    """
    Test suite for running pace math and race time predictions.
    """

    def setUp(self):
        
        self.calc = PacingCalculator()

    def test_calculate_pace(self):
        """
        Checks if decimal pace and MM:SS formatting calculate correctly.
        """
    
        result = self.calc.calculate_pace(3.0, 30.0)
        
        self.assertEqual(result["decimal"], 10.0)
        self.assertEqual(result["formatted"], "10:00")
        
        
        result_uneven = self.calc.calculate_pace(10.0, 75.5)
        self.assertEqual(result_uneven["decimal"], 7.55)
        self.assertEqual(result_uneven["formatted"], "7:33")

    def test_predict_race_times(self):
        """
        Checks if standard race finish times predict correctly based on pace.
        """
       
        predictions = self.calc.predict_race_times(10.0)
        
        
        self.assertEqual(predictions["5K"]["hours"], 0)
        self.assertEqual(predictions["5K"]["minutes"], 31)
        self.assertEqual(predictions["5K"]["seconds"], 0)
        
        
        self.assertEqual(predictions["Half Marathon"]["hours"], 2)
        self.assertEqual(predictions["Half Marathon"]["minutes"], 11)
        self.assertEqual(predictions["Half Marathon"]["seconds"], 0)

if __name__ == '__main__':
    unittest.main()