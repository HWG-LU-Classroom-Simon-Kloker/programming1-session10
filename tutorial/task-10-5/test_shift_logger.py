"""
Tests for the Red Cross Volunteer Shift Logger.
Demonstrates proper testing with pytest fixtures.
"""

import pytest
from shift_logger import Volunteer, log_arrival


# ============================================
# FIXTURES (Test Setup)
# ============================================

@pytest.fixture
def sample_volunteer():
    """Create a sample volunteer for testing."""
    return Volunteer("Clara Barton", "Morning")


@pytest.fixture
def multiple_volunteers():
    """Create multiple volunteers for testing."""
    return [
        Volunteer("Henry Dunant", "Morning"),
        Volunteer("Florence Nightingale", "Afternoon"),
        Volunteer("Jean-Henri Dunant", "Evening")
    ]


# ============================================
# TEST FUNCTIONS
# ============================================

def test_volunteer_creation():
    """Test that a Volunteer instance can be created with correct attributes."""
    volunteer = Volunteer("Clara Barton", "Morning")
    
    assert volunteer.name == "Clara Barton"
    assert volunteer.shift_time == "Morning"


def test_volunteer_with_fixture(sample_volunteer):
    """Test volunteer attributes using a fixture."""
    assert sample_volunteer.name == "Clara Barton"
    assert sample_volunteer.shift_time == "Morning"


def test_volunteer_repr(sample_volunteer):
    """Test the string representation of a Volunteer."""
    expected = "Volunteer(name='Clara Barton', shift_time='Morning')"
    assert repr(sample_volunteer) == expected


def test_log_arrival_executes(sample_volunteer, capsys):
    """Test that log_arrival function runs without errors and produces output."""
    # Call the function
    log_arrival(sample_volunteer)
    
    # Capture the printed output
    captured = capsys.readouterr()
    
    # Verify the output contains the volunteer's information
    assert "Clara Barton" in captured.out
    assert "Morning" in captured.out
    assert "✅" in captured.out


def test_log_arrival_with_different_shifts():
    """Test that log_arrival works with different shift times."""
    shifts = ["Morning", "Afternoon", "Evening", "Night"]
    
    for shift in shifts:
        volunteer = Volunteer("Test Volunteer", shift)
        # Should not raise any errors
        log_arrival(volunteer)


def test_multiple_volunteers_logging(multiple_volunteers, capsys):
    """Test logging multiple volunteers in sequence."""
    for volunteer in multiple_volunteers:
        log_arrival(volunteer)
    
    captured = capsys.readouterr()
    
    # Verify all volunteers were logged
    assert "Henry Dunant" in captured.out
    assert "Florence Nightingale" in captured.out
    assert "Jean-Henri Dunant" in captured.out


# ============================================
# BONUS: Testing Edge Cases
# ============================================

def test_volunteer_with_special_characters():
    """Test that volunteers with special characters in names work correctly."""
    volunteer = Volunteer("José María", "Afternoon")
    assert volunteer.name == "José María"


def test_volunteer_with_long_name():
    """Test that long volunteer names are handled correctly."""
    long_name = "Dr. Florence Emma Nightingale-Davidson III"
    volunteer = Volunteer(long_name, "Evening")
    assert volunteer.name == long_name


def test_different_shift_formats():
    """Test that various shift time formats are accepted."""
    shift_formats = ["Morning", "morning", "MORNING", "9:00-17:00", "Early Morning"]
    
    for shift in shift_formats:
        volunteer = Volunteer("Test Person", shift)
        assert volunteer.shift_time == shift
