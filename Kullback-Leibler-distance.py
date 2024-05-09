import numpy as np
from Huffman.Huffman import *
import colorama
from colorama import Fore, Style

colorama.init()

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
        KL_divergence += p[char] * np.log(p[char]/q[char])

    return KL_divergence

def get_frequencies(sequence, distribution):
    frequencies = {}
    symbols = distribution.keys()
    for symbol in symbols:
        frequencies[symbol] = 0

    for symbol in sequence:
        frequencies[symbol] += 1

    return list(frequencies.values()), list(symbols)


def generate_huffman_sequence(sequence, huffman_codes):
    code = ""
    for symbol in sequence:
        code += huffman_codes[symbol]

    return code

# define the distributions
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
    "d": 1/16,
    "e": 1/2
}

sequence_length = 1000
random_sequence = generate_random_sequence_with_distribution(distribution, sequence_length)

frequencies, symbols = get_frequencies(random_sequence, distribution)

# Build the Huffman tree
root = build_huffman_tree(symbols, frequencies)

# Generate Huffman codes
huffman_codes = generate_huffman_codes(root)

huffman_sequence = generate_huffman_sequence(random_sequence,huffman_codes)

sequence_length = len(huffman_sequence)
compression_ratio = len(random_sequence) / sequence_length
print("Sequences:")
print("Unencoded Sequence:", random_sequence)
print("Huffman Encoded Sequence:", huffman_sequence)
print()
print("Values:")
print("Symbols:", symbols)
print("Frequencies:", frequencies)
print("Distribution:", distribution)
print("Encoded Sequence Length:", sequence_length)
print("Compression Ratio: {:.2f}".format(compression_ratio))
print()

# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")
print()

KL_divergence = kullback_leibler_distance(distribution,distribution2,random_sequence)
KL_divergence_opposite = kullback_leibler_distance(distribution2,distribution,random_sequence)

print("KL divergence:", KL_divergence)
print("KL divergence with switched a and e probabilities:", KL_divergence_opposite)

# generate switched probabilty sequence
random_sequence2 = generate_random_sequence_with_distribution(distribution2, sequence_length)

frequencies, symbols = get_frequencies(random_sequence2, distribution)

# Build the Huffman tree
root = build_huffman_tree(symbols, frequencies)

# Generate Huffman codes
huffman_codes = generate_huffman_codes(root)

# generate old sequence based on new huffman tree
huffman_sequence = generate_huffman_sequence(random_sequence,huffman_codes)


sequence_length2 = len(huffman_sequence)
compression_ratio2 = len(random_sequence) / sequence_length2

print()
print("New Huffman Encoded Sequence:", huffman_sequence)
print()
print("Values:")
print("Symbols:", symbols)
print("Frequencies:", frequencies)
print("Distribution:", distribution2)
print("New Encoded Sequence Length:", sequence_length2)
print("New Compression Ratio: {:.2f}".format(compression_ratio2))
print()
print("Differences:")
print("Length comparison:", "optimal "+Fore.GREEN + str(sequence_length) + Style.RESET_ALL,"switched "+ Fore.RED + str(sequence_length2) + Style.RESET_ALL, "difference "+Fore.YELLOW + str(sequence_length2-sequence_length) + Style.RESET_ALL,  )
print("Compression Rate comparison:", "optimal "+Fore.GREEN + str(compression_ratio) + Style.RESET_ALL,"switched "+ Fore.RED + str(compression_ratio2) + Style.RESET_ALL, "difference "+Fore.YELLOW + str(compression_ratio-compression_ratio2) + Style.RESET_ALL,  )