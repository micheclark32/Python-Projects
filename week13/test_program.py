from password_generator import password_props
from password_generator import generate
import pytest


def test_generate():
    ran_numbers = []

    generate(ran_numbers)

    assert len(ran_numbers) >= 8


def test_password_props():
    ran_words = []

    password_props(ran_words)

    assert len(ran_words) >= 1


pytest.main(["-v", "--tb=line", "-rN", __file__])
