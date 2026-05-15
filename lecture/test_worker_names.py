from worker_names import get_formatted_worker_name

def test_simple_worker_name():
    """
    Test that simple worker names (first and last) are formatted correctly.
    Example: Clara Barton
    """
    formatted_name = get_formatted_worker_name('clara', 'barton')
    assert formatted_name == 'Clara Barton'
