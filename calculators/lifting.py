"""
Module: calculators.lifting
Purpose: Handles barbell percentage math and generates training blocks.
"""

class LiftingCalculator:
    """
    A 4-week strength training block based on an athlete's one-rep max for declared exercise(s).
    """

    def __init__(self):
        # The base 4-week progression template stored as a class attribute
        self.progression_template = {
            "Week 1 (65%)": (0.65, "8-10 reps"),
            "Week 2 (75%)": (0.75, "5-7 reps"),
            "Week 3 (85%)": (0.85, "3-5 reps"),
            "Week 4 (Deload)": (0.50, "10-12 reps")
        }
    
    def calculate_block(self, max_weight):
       
        """
        Takes a 1RM and returns a dictionary of weekly target weights and rep ranges.
        """
       
        calculated_block = {}
        
        for week, (percent, reps) in self.progression_template.items():
            target_weight = round(max_weight * percent, 2)
            calculated_block[week] = {
                "weight": target_weight, 
                "target": reps
            }
            
        return calculated_block