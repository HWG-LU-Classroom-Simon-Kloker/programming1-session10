class VolunteerSurvey:
    """Collect anonymous survey responses from Red Cross volunteers."""
    
    def __init__(self, question):
        """Store a survey question and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Display the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single volunteer response."""
        if not new_response:
            raise ValueError("Response cannot be empty.")
        self.responses.append(new_response)
    
    def show_results(self):
        """Display all responses received."""
        print("Survey Results:")
        for response in self.responses:
            print(f"- {response}")
