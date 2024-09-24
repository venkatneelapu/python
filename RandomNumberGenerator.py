import random

# Generate a random integer between 1 and 100
random_integer = random.randint(1, 100)
print("Random Integer:", random_integer)

# Generate a random floating-point number between 0 and 1
random_float = random.random()
print("Random Float:", random_float)

# Generate a random number between a range of floats (e.g., 1.5 to 6.5)
random_float_range = random.uniform(1.5, 6.5)
print("Random Float in range:", random_float_range)
