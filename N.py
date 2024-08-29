height = 7  # Height of the alphabet "N"
width = height  # Width is the same as height

for i in range(height):
    for j in range(width):
        # Print stars at the start and end of the row
        if j == 0 or j == width - 1:
            print("*", end="")
        # Print stars in the diagonal to form the "N"
        elif i == j:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # New line after each row
