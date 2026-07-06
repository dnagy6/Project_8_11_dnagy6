"""
Module: calculators.pacing
Purpose: Handles running pace math and race time predictions.
"""

class PacingCalculator:
    """Calculates mile paces and predicts standard race finish times."""

    def __init__(self):
        self.race_distances = {
            "5K": 3.1,
            "10K": 6.2,
            "Half Marathon": 13.1,
            "Marathon": 26.2
        }

    def calculate_pace(self, distance, time_minutes):
        """
        Calculates the pace per mile returning both decimal and MM:SS formats.
        """
        pace_decimal = time_minutes / distance
        
        # Convert decimal pace to minutes and seconds
        pace_mins = int(pace_decimal)
        pace_secs = int((pace_decimal - pace_mins) * 60)
        
        return {
            "decimal": pace_decimal,
            "formatted": f"{pace_mins}:{pace_secs:02d}"
        }

    def predict_race_times(self, pace_decimal):
        """
        Calculates finish times for standard races based on a decimal pace in HH:MM:SS format.
        """
        predictions = {}
        
        for race, miles in self.race_distances.items():
            total_minutes = pace_decimal * miles
            
            hours = int(total_minutes // 60)
            mins = int(total_minutes % 60)
            secs = int((total_minutes - int(total_minutes)) * 60)
            
            predictions[race] = {
                "miles": miles,
                "hours": hours,
                "minutes": mins,
                "seconds": secs
            }
            
        return predictions