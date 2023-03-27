# Genetic Algorithm Implementation
# Full code by Saurav Adhikari <github.com/ersauravadhikari>
import math

import numpy as np

from consts import POPULATION_SIZE
from models import Individual

# Setting up the default environment
play_environment = np.zeros((8, 7))

# The individual in this scenario is the rules
current_population = []

for _ in range(POPULATION_SIZE):
    ind = Individual.generate_random()
    current_population.append(ind)


def population_selection(population):
    """
    Does genetic selection
    :return: selected population
    """

    """
    # 10% is elite
    # 10% is random generation
    # Remaining is tournament
    """

    sorted_current = sorted(current_population, key=lambda x: x.fitness, reverse=True)

    ten_percentage = math.floor(POPULATION_SIZE / 10)
    elite = sorted_current[0:ten_percentage]
    random_ones = [Individual.generate_random() for _ in range(ten_percentage)]
    scp = sorted_current[0: POPULATION_SIZE - 2 * ten_percentage]

    sel_pop = Individual.selection(scp)
    return sel_pop + elite + random_ones


# Default Setup
# new_population = current_population
best = Individual.find_best(current_population)

itr_count = 0

while best.fitness < 1:
    # A simple check to see that the random population generation is indeed working

    itr_count += 1

    # Selection method
    selected_population = population_selection(current_population)

    # Mutation
    for ind in selected_population:
        ind.mutate()

    # Crossover
    new_gen = Individual.crossover(selected_population)

    # Mutation
    for ind in new_gen:
        ind.mutate()

    current_population = new_gen
    new_best = Individual.find_best(new_gen)
    best = new_best

    print(f"The best individual in generation {itr_count} is: {best.fitness}")

print("Found Solution: ", best.rules)
