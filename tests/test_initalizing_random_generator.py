import pytest

from src.random_generator.random_number import RandomGenerator


def test_initializing_generator_with_difference_in_size_of_given_elements():
    with pytest.raises(ValueError):
        RandomGenerator([1, 2, 3], [1])


def test_initializing_generator_with_probability_diff_than_1():
    with pytest.raises(ValueError):
        RandomGenerator([1, 2, 3], [0.1, 0.4, 0.3])
