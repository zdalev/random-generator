import pytest

from src.random_generator.random_number import RandomGenerator


def test_initializing_generator_with_difference_in_size_of_given_elements():
    with pytest.raises(ValueError):
        RandomGenerator([1, 2, 3], [1])


def test_initializing_generator_with_probability_diff_than_1():
    with pytest.raises(ValueError):
        RandomGenerator([1, 2, 3], [0.1, 0.4, 0.3])


@pytest.fixture
def random_generator():
    generator = RandomGenerator([-1, 0, 1, 2, 3], [0.01, 0.3, 0.58, 0.1, 0.01])
    return generator


@pytest.fixture
def populate_generator(random_generator):
    for _ in range(100):
        random_generator.next_num()

    return random_generator


def test_number_distribution(populate_generator):
    results = populate_generator.results
    for number, occurrences in results.items():
        prob_number = populate_generator.prop_per_number.get(number)
        assert occurrences / 100 == pytest.approx(prob_number, rel=0.05, abs=0.05)


def test_next_num_in_numbers(random_generator):
    for _ in range(100):
        assert random_generator.next_num() in [-1, 0, 1, 2, 3]
