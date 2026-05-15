class DuplicateCountryError(Exception):
    """Custom error for the historical integrity of the treaty."""
    pass

class Delegation:
    """Represents a country's delegation to the Geneva Convention."""
    def __init__(self, name, is_neutral=False):
        # Normalization logic: Clean the "OCR" messiness
        self.name = name.strip().title()
        self.is_neutral = is_neutral

class Convention:
    """Manages the delegations and votes for the Geneva Convention."""
    def __init__(self):
        self.delegations = {}

    def add_delegation(self, delegation):
        """Adds a delegation to the convention, ensuring no duplicates."""
        if delegation.name in self.delegations:
            raise DuplicateCountryError(f"{delegation.name} is already a signatory.")
        self.delegations[delegation.name] = delegation

    def total_votes(self):
        """Calculates the total votes for the convention."""
        count = 0
        for country in self.delegations.values():
            if country.is_neutral:
                count += 2
            else:
                count += 1
        return count
