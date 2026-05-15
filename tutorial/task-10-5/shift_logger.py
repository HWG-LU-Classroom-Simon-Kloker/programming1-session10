"""
Red Cross Volunteer Shift Logger
A demonstration of proper Python program structure with the main guard pattern.
"""

# ============================================
# ZONE 1: IMPORTS
# ============================================
from datetime import datetime


# ============================================
# ZONE 2: DEFINITIONS (Classes & Functions)
# ============================================

class Volunteer:
    """Represent a Red Cross volunteer with name and shift information."""
    
    def __init__(self, name, shift_time):
        """
        Initialize a volunteer.
        
        Args:
            name (str): The volunteer's name
            shift_time (str): The shift time (e.g., 'Morning', 'Afternoon', 'Evening')
        """
        self.name = name
        self.shift_time = shift_time
    
    def __repr__(self):
        """Return a string representation of the volunteer."""
        return f"Volunteer(name='{self.name}', shift_time='{self.shift_time}')"


def log_arrival(volunteer):
    """
    Log when a volunteer arrives for their shift.
    
    Args:
        volunteer (Volunteer): The volunteer who arrived
    """
    print(f"✅ {volunteer.name} arrived for {volunteer.shift_time} shift")


# ============================================
# ZONE 3: EXECUTION (Main Function)
# ============================================

def main():
    """Entry point of the program when run directly."""
    print("\n" + "="*60)
    print("🏥 Red Cross Volunteer Shift Logger - Starting Up")
    print("="*60 + "\n")
    
    # Create volunteer instances
    volunteers = [
        Volunteer("Clara Barton", "Morning"),
        Volunteer("Henry Dunant", "Afternoon"),
        Volunteer("Florence Nightingale", "Evening")
    ]
    
    # Log each arrival
    print("📋 Logging volunteer arrivals:\n")
    for volunteer in volunteers:
        log_arrival(volunteer)
    
    # Summary
    print(f"\n✨ Total volunteers logged today: {len(volunteers)}")
    print(f"⏰ Logging completed at: {datetime.now().strftime('%H:%M:%S')}")
    
    print("\n" + "="*60)
    print("🏥 Red Cross Volunteer Shift Logger - Shutting Down")
    print("="*60 + "\n")


# The "Front Door" - Only opens when file is run directly
if __name__ == "__main__":
    main()
