import dataclasses
import math
import random
import numpy

PROBABILITY_TOLERANCE = 1e-16


@dataclasses.dataclass
class RandomGenerator:
    # Values that may be returned by next_num()
    numbers: list
    # Probability of the occurrence of random_nums
    probabilities: list

    def __post_init__(self):
        """ Adding constrains """
        if len(self.numbers) != len(self.probabilities):
            raise ValueError('The number of given numbers and probabilities must match.')
        probability_sum = sum(self.probabilities)

        if not math.isclose(1.0,probability_sum , rel_tol=PROBABILITY_TOLERANCE):
            raise ValueError(f'Probabilities must sum up to 1. Current sum is {probability_sum}.')

    def next_num(self):
        """
        Returns one of the random_nums. When this method is called multiple
        times over a long period, it should return the numbers roughly with
        the initialized probabilities.
        """
        result = numpy.random.choice(self.numbers, size=1, p=self.probabilities).item()
        return result

    @property
    def prop_per_number(self):
        return dict(zip(self.numbers, self.probabilities))


@dataclasses.dataclass
class NumberContainer:
    generator: RandomGenerator
    container: dict = dataclasses.field(default_factory=dict)

    def populate_container(self, given_range: int) -> None:
        for _ in range(given_range):
            number = self.generator.next_num()
            if self.container.get(number):
                self.container[number] += 1
                continue
            self.container[number] = 1


if __name__ == '__main__':
    given_numbers = [-1, 0, 1, 2, 3]
    probabilities = [0.01, 0.3, 0.58, 0.1, 0.01]
    generator = RandomGenerator(given_numbers, probabilities)
    print('Probability per number: ', generator.prop_per_number)
    number_container = NumberContainer(generator)

    number_container.populate_container(100)

    print(f'Container: {number_container.container}')
