# Example: Using the VolunteerSurvey class

from red_cross_survey import VolunteerSurvey

# Create survey
question = "What humanitarian region do you work in?"
survey = VolunteerSurvey(question)

# Collect responses
survey.show_question()
survey.store_response('Southeast Asia')
survey.store_response('Middle East')
survey.store_response('Africa')

# Show results
survey.show_results()
