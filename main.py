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
                
                
                estimated_max = lifting_calc.estimate_1rm(weight, reps)
                user_maxes[lift_name] = estimated_max
                storage.save_data(user_maxes)

                
                block = lifting_calc.calculate_block(estimated_max)
                print(f"\n--- 4-Week Training Block for {estimated_max} lbs ---")
                
                for week, data in block.items():
                    print(f"{week}: {data['weight']} lbs | Target: {data['target']}")
                    
            except ValueError:
                print("Invalid input. Please enter numeric values for weight and reps.")

        elif choice == '2':
            try:
                distance = float(input("Enter the total distance of your run (in miles): "))
                time_mins = float(input("Enter your total time for the run (in minutes): "))
                
                
                pace_data = pacing_calc.calculate_pace(distance, time_mins)
                print(f"\nYour baseline pace is: {pace_data['formatted']} / mile")
                
                
                predictions = pacing_calc.predict_race_times(pace_data['decimal'])
                print("\n--- Estimated Race Finish Times ---")
                
                for race, data in predictions.items():
                    if data['hours'] > 0:
                        print(f"{race} ({data['miles']} mi): {data['hours']}h {data['minutes']:02d}m {data['seconds']:02d}s")
                    else:
                        print(f"{race} ({data['miles']} mi): {data['minutes']}m {data['seconds']:02d}s")
                        
            except ValueError:
                print("Invalid input. Please enter numeric values.")

        elif choice == '3':
            if user_maxes:
                print("\n--- Stored Maxes ---")
                for lift, max_weight in user_maxes.items():
                    print(f"{lift}: {max_weight} lbs")
            else:
                print("No maxes stored yet. Use the Lifting Calculator to add your maxes.")

        elif choice == '4':
            print(f"\n[Session maxes stored: {user_maxes}]")
            print("Exiting the program. Goodbye!")
            running = False
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()