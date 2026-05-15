class ReliefWorker:
    """Represent a Red Cross relief worker."""
    
    def __init__(self, first_name, last_name, annual_salary):
        """Initialize the worker with name and salary."""
        self.first_name = first_name
        self.last_name = last_name
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount=5000):
        """Give the worker a raise."""
        self.annual_salary += raise_amount
