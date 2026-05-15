class DuplicateCountryError(Exception):
    """Raised when a country tries to sign the convention more than once."""
    pass

class Delegation:
    """Represents a country's delegation to the Geneva Convention."""
    def __init__(self, name, is_neutral=False):
        # TODO: Normalize name here (strip and title case)
        self.name = name
        self.is_neutral = is_neutral

class Convention:
    """Manages the delegations and votes for the Geneva Convention."""
    def __init__(self):
        self.delegates = {}

    def add_delegation(self, delegation):
        """Adds a delegation to the convention, ensuring no duplicates."""
        if delegation.name in self.delegates:
            raise DuplicateCountryError(f"{delegation.name} is already signed.")
        self.delegates[delegation.name] = delegation

    def total_votes(self):
        """Calculates the total votes for the convention."""
        # TODO: Implement this method. 
        # Neutral = 2 votes, Others = 1 vote.
        pass
