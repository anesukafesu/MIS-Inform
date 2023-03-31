#!/usr/bin/env python3

import numpy as np

# Generate population data
population = np.random.randint(low=100000, high=1000000, size=1000)

# Calculate statistics
mean_pop = np.mean(population)
median_pop = np.median(population)
max_pop = np.max(population)
min_pop = np.min(population)

# Print results
print('Population Statistics:')
print('----------------------')
print(f'Mean Population: {mean_pop:.2f}')
print(f'Median Population: {median_pop:.2f}')
print(f'Maximum Population: {max_pop:,}')
print(f'Minimum Population: {min_pop:,}')
