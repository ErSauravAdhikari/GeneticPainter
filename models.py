import random

import numpy as np

from consts import MUTATION_RATE, CROSSOVER_RATE, ENVIRONMENT_SIZE
from painter_play import painter_play


class Individual:
    def __init__(self, rules, environment=None):
        self._rules = rules
        self._environment = environment if environment is not None else np.zeros(ENVIRONMENT_SIZE)
        self._cached_fitness = self._fitness_calc()

    def _fitness_calc(self):
        play_environment = np.copy(self._environment)

        # print(play_environment)
        score, _, _ = painter_play(self._rules, play_environment)
        return score

    def mutate(self):
        if random.random() > MUTATION_RATE:
            return

        # A random portion is taken, and it's value is changed
        gene = random.randrange(0, len(self._rules))
        self._rules[gene] = random.randint(0, 3)

        # We must reset the fitness cache after mutation
        self.reset_fitness()

    def reset_fitness(self):
        self._cached_fitness = self._fitness_calc()

    @property
    def rules(self):
        return self._rules

    @property
    def fitness(self):
        return self._cached_fitness

    @staticmethod
    def crossover(population):
        # Divide population into two
        pop_size = len(population)

        new_generation = []

        parents_1 = [population[i] for i in range(pop_size) if i % 2 == 0]
        parents_2 = [population[i] for i in range(pop_size) if i % 2 == 1]

        for i in range(len(parents_1)):
            p1 = parents_1[i]
            p2 = parents_2[i]

            if random.random() > CROSSOVER_RATE:
                new_generation.append(p1)
                new_generation.append(p2)
                continue

            rules_size = len(p1.rules)
            c1 = [p1.rules[i] if i % 2 == 0 else p2.rules[i] for i in range(rules_size)]
            c2 = [p1.rules[i] if i % 2 == 1 else p2.rules[i] for i in range(rules_size)]

            new_generation.append(Individual(c1))
            new_generation.append(Individual(c2))

        return new_generation

    @staticmethod
    def generate_random(environment=None):
        r = [1] * 54
        r = np.array(r)
        for i in range(len(r)):
            r[i] = random.randint(0, 3)
        ind = Individual(rules=r, environment=environment)
        return ind

    @staticmethod
    def selection(population):
        new_population = []
        pop_size = len(population)

        for i in range(pop_size):
            # Tournament only selection
            p1 = random.sample(population, 1)[0]
            p2 = random.sample(population, 1)[0]
            p3 = random.sample(population, 1)[0]

            best = Individual.find_best([p1, p2, p3])
            new_population.append(best)
            # print(f"best among, {p1.fitness}, {p2.fitness}, {p3.fitness} is {best.fitness}")

        return new_population

    @staticmethod
    def find_best(population):
        return max(population, key=lambda x: x.fitness)
