from relief_worker import ReliefWorker

def test_give_default_raise():
    """Test that default raise of $5,000 is applied."""
    worker = ReliefWorker('Clara', 'Barton', 40000)
    worker.give_raise()
    assert worker.annual_salary == 45000

def test_give_custom_raise():
    """Test that custom raise amount is applied."""
    worker = ReliefWorker('Florence', 'Nightingale', 50000)
    worker.give_raise(3000)
    assert worker.annual_salary == 53000
