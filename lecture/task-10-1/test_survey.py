from red_cross_survey import VolunteerSurvey

def test_store_single_response():
    """Test that a single response is stored properly."""
    question = "What humanitarian region do you work in?"
    survey = VolunteerSurvey(question)
    
    # Store a single response
    survey.store_response('Africa')
    
    # Verify it was stored
    assert 'Africa' in survey.responses

def test_store_three_responses():
    """Test that multiple responses are stored properly."""
    question = "What humanitarian region do you work in?"
    survey = VolunteerSurvey(question)
    
    # Store multiple responses
    responses = ['Southeast Asia', 'Middle East', 'Africa']
    for response in responses:
        survey.store_response(response)
    
    # Verify all were stored
    for response in responses:
        assert response in survey.responses
