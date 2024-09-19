import pytest

from random_generator.random_number import RandomGenerator


@pytest.fixture
def generator():
    return RandomGenerator([1, 2, 3], [0.33, 0.34, 0.33])


def test_next_num(generator):
    assert generator.next_num() in [1, 2, 3]


def test_probability_per_number(generator):
    assert generator.prop_per_number == {1: 0.33,
                                         2: 0.34,
                                         3: 0.33}
