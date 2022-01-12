from names import make_full_name, extract_given_name, extract_family_name
import pytest


def test_make_full_name():
    """Verify that the make_full_name function returns correct results."""
    assert make_full_name("Michael", " Clark-Hirz") == "Clark-Hirz; Michael"
    assert make_full_name("Michael", "Clark") == "Clark; Michael"
    assert make_full_name("Mr", "C") == "C; Mr"
    assert make_full_name("", "") == "; "


def test_extract_family_name():
    """Verify that the extract_family_name function returns correct results."""
    assert extract_family_name("Clark-Hirz; Michael") == "Clark-Hirz"
    assert extract_family_name("Clark; Michael") == "Clark"
    assert extract_family_name("Mr; C") == "Mr"
    assert extract_family_name("; ") == ""


def test_extract_given_name():
    """Verify that the extract_given_name function returns correct results."""
    assert extract_given_name("Clark-Hirz; Michael") == "Michael"
    assert extract_given_name("Clark; Michael") == "Michael"
    assert extract_given_name("Mr; C") == "C"
    assert extract_given_name("; ") == ""


# Call the main function that is part of pytest so that
# the test functions in this file will start executing.
pytest.main(["-v", "--tb=line", "-rN", "test_names.py"])
