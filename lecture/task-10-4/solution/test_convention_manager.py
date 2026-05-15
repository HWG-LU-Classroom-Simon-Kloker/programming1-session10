import pytest
from convention_manager import Delegation, Convention, DuplicateCountryError

# --- FIXTURES ---
@pytest.fixture
def empty_convention():
    return Convention()

@pytest.fixture
def standard_meeting(empty_convention):
    """A fixture that provides a convention with two specific countries."""
    empty_convention.add_delegation(Delegation("France", is_neutral=False))
    empty_convention.add_delegation(Delegation("Switzerland", is_neutral=True))
    return empty_convention

# --- TESTS ---

@pytest.mark.parametrize("raw_input, expected", [
    ("  belgium  ", "Belgium"),
    ("DENMARK", "Denmark"),
    ("  pruSSia", "Prussia")
])
def test_name_normalization(raw_input, expected):
    d = Delegation(raw_input)
    assert d.name == expected

def test_duplicate_prevention(standard_meeting):
    # Try to add Switzerland again
    with pytest.raises(DuplicateCountryError):
        standard_meeting.add_delegation(Delegation("Switzerland"))

def test_voting_logic(standard_meeting):
    # France (1) + Switzerland (2) should = 3
    assert standard_meeting.total_votes() == 3

def test_empty_convention_votes(empty_convention):
    assert empty_convention.total_votes() == 0
