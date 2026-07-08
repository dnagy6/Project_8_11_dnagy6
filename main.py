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

    while running:
        print("\n--- Hybrid Training & Pace Calculator ---")
        print("Please select an option:")
        print("1. Lifting Calculator (Barbell Percentages)")
        print("2. Pacing Calculator (Running Splits & Race Predictions)")
        print("3. View Stored Maxes")
        print("4. Exit")

        choice = input("Enter your choice (1, 2, 3, or 4): ")

        if choice == '1':
        

        elif choice == '2':
        

        elif choice == '3':
        

        elif choice == '4':
            print(f"\n[Session maxes stored: {user_maxes}]")
            print("Exiting the program. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()