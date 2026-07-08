"""
Program: Hybrid Training & Pace Calculator
Author: Dakota Nagy
Purpose: This main.py is a terminal utility to calculate barbell percentages
         and running pacing splits.
"""

from data.storage import DataStorage
from calculators.lifting import LiftingCalculator
from calculators.pacing import PacingCalculator

def main():
    """
    Main entry point for the Hybrid Training & Pace Calculator.
    """
    storage = DataStorage()
    lifting_calc = LiftingCalculator()
    pacing_calc = PacingCalculator()

    user_maxes = storage.load_data()
    running = True