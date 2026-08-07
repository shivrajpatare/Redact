import math

from redact.utils import calculate_shannon_entropy


def test_empty_string_returns_zero():
    assert calculate_shannon_entropy("") == 0


def test_uniform_string_has_zero_entropy():
    assert calculate_shannon_entropy("aaaaaa") == 0


def test_known_entropy_value():
    # Two equally likely symbols -> exactly 1 bit of entropy
    assert math.isclose(calculate_shannon_entropy("ab"), 1.0, rel_tol=1e-9)


def test_high_entropy_random_string_exceeds_threshold():
    random_looking = "aB3!kZ9#mQ7$pL2@rT5&nW8*"
    assert calculate_shannon_entropy(random_looking) > 4.5
