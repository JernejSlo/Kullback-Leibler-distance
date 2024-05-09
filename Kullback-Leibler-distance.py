from random import random
import numpy as np

distribution = {
    "a": 1/2,
    "b": 1/4,
    "c": 1/8,
    "d": 1/16,
    "e": 1/16
}


def generate_random_sequence_with_distribution(distribution, length):
    # Extract the keys (characters) and their corresponding probabilities from the distribution dictionary
    characters = list(distribution.keys())
    probabilities = list(distribution.values())

    # Generate the sequence by randomly choosing characters according to the defined probabilities
    sequence = np.random.choice(characters, size=length, p=probabilities)

    return ''.join(sequence)  # Convert array to string for easier use

    # Example usage


sequence_length = 20
random_sequence = generate_random_sequence_with_distribution(distribution, sequence_length)
print(random_sequence)