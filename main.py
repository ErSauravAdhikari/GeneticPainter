# Genetic Algorithm Implementation
# Full code by Saurav Adhikari <github.com/ersauravadhikari>

import numpy as np

from models import Individual

# Setting up the default environment
play_environment = np.zeros((8, 7))

# The individual in this scenario is the rules
current_population = []

for _ in range(100):
    ind = Individual.generate_random()
    current_population.append(ind)

# Default Setup
# new_population = current_population
best = Individual.find_best(current_population)
while best.fitness < 1:
    # A simple check to see that the random population generation is indeed working

    # Selection
    selected_population = Individual.selection(current_population)

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

    print(f"BEST IS: {best.fitness}")

print("Found Solution: ", best.rules)
