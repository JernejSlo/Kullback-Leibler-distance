import numpy as np
from Huffman.Huffman import *
import colorama
from colorama import Fore, Style

colorama.init(autoreset=True)
def generate_random_sequence_with_distribution(distribution, length):
    # Extract the keys (characters) and their corresponding probabilities from the distribution dictionary
    characters = list(distribution.keys())
    probabilities = list(distribution.values())

    # Generate the sequence by randomly choosing characters according to the defined probabilities
    sequence = np.random.choice(characters, size=length, p=probabilities)

    return ''.join(sequence)  # Convert array to string for easier use

def kullback_leibler_distance(p, q):
    KL_divergence = 0
    for char in p:
        if p[char] > 0:  # Only calculate if p[char] is greater than 0
            if q[char] > 0:
                KL_divergence += p[char] * np.log(p[char] / q[char])
            else:
                return float('inf')  # Return infinity if q[char] is 0 and p[char] is not
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
print(Style.BRIGHT +"Sequences:")
print(Style.BRIGHT +"Unencoded Sequence:", random_sequence)
print(Style.BRIGHT +"Huffman Encoded Sequence:", huffman_sequence)
print()
print(Style.BRIGHT +"Values:")
print(Style.BRIGHT +"Symbols:", symbols)
print(Style.BRIGHT +"Frequencies:", frequencies)
print(Style.BRIGHT +"Distribution:", distribution)
print(Style.BRIGHT +"Encoded Sequence Length:", Fore.GREEN + str(sequence_length))
print(Style.BRIGHT +"Compression Ratio:",Fore.GREEN + str(compression_ratio))
print()
print(Style.BRIGHT +"Huffman with original probability distribution")
# Print Huffman codes
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")
print()

KL_divergence = kullback_leibler_distance(distribution,distribution2)
KL_divergence_opposite = kullback_leibler_distance(distribution2,distribution)

print(Style.BRIGHT +"KL divergence:", KL_divergence)
print(Style.BRIGHT +"KL divergence with switched a and e probabilities:", KL_divergence_opposite)

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
print(Style.BRIGHT +"New Huffman tree with switched probability distribution")
for char, code in huffman_codes.items():
    print(f"Character: {char}, Code: {code}")

print()
print(Style.BRIGHT +"New Huffman Encoded Sequence:", huffman_sequence)
print()
print(Style.BRIGHT +"Values:")
print(Style.BRIGHT +"Symbols:", symbols)
print(Style.BRIGHT +"Frequencies:", frequencies)
print(Style.BRIGHT +"Distribution:", distribution2)
print(Style.BRIGHT +"New Encoded Sequence Length:", Fore.RED + str(sequence_length2))
print(Style.BRIGHT +"New Compression Ratio:",(Fore.RED + str(compression_ratio2)))
print()
print(Style.BRIGHT +"Differences:")
print(Style.BRIGHT +"Length comparison:", "optimal "+Fore.GREEN + str(sequence_length) ,"switched "+ Fore.RED + str(sequence_length2) , "difference "+Fore.YELLOW + str(sequence_length2-sequence_length) ,  )
print(Style.BRIGHT +"Compression Rate comparison:", "optimal "+Fore.GREEN + str(compression_ratio) ,"switched "+ Fore.RED + str(compression_ratio2) , "difference "+Fore.YELLOW + str(compression_ratio-compression_ratio2) ,  )