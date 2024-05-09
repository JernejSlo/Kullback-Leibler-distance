import math
from random import random
import numpy as np

distribution = {
    "a": 1/2,
    "b": 1/4,
    "c": 1/8,
    "d": 1/16,
    "e": 1/16
}
distribution2 = {
    "a": 1/16,
    "b": 1/4,
    "c": 1/8,
    "d": 1/2,
    "e": 1/16
}
def generate_random_sequence_with_distribution(distribution, length):
    # Extract the keys (characters) and their corresponding probabilities from the distribution dictionary
    characters = list(distribution.keys())
    probabilities = list(distribution.values())

    # Generate the sequence by randomly choosing characters according to the defined probabilities
    sequence = np.random.choice(characters, size=length, p=probabilities)

    return ''.join(sequence)  # Convert array to string for easier use

def kullback_leibler_distance(p,q,sequence):
    KL_divergence = 0
    character_array = list(sequence)

    for char in character_array:
        KL_divergence += p[char] * math.log2(p[char]/q[char])

    return KL_divergence


sequence_length = 1000
random_sequence = generate_random_sequence_with_distribution(distribution, sequence_length)

KL_divergence = kullback_leibler_distance(distribution,distribution2,random_sequence)
print(KL_divergence)