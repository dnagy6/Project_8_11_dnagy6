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
            try:
                lift_name = input("Enter the lift name (e.g., Squat, Bench Press): ").title()
                weight = float(input("Enter the weight lifted (in lbs): "))
                reps = int(input("Enter reps completed (Type 1 if this was a true max): "))
                
                
                estimated_max = lift_calc.estimate_1rm(weight, reps)
                user_maxes[lift_name] = estimated_max
                storage.save_data(user_maxes)

                
                block = lift_calc.calculate_block(estimated_max)
                print(f"\n--- 4-Week Training Block for {estimated_max} lbs ---")
                
                for week, data in block.items():
                    print(f"{week}: {data['weight']} lbs | Target: {data['target']}")
                    
            except ValueError:
                print("Invalid input. Please enter numeric values for weight and reps.")

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