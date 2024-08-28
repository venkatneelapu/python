height = 7  # Height of the alphabet "M"
width = height  # Width is the same as height

for i in range(height):
    for j in range(width):
        # Print stars at the start and end of the row
        if j == 0 or j == width - 1:
            print("*", end="")
        # Print stars in the middle to form the diagonal arms of "M"
        elif i == j and j <= width // 2:
            print("*", end="")
        elif j == width - i - 1 and j >= width // 2:
            print("*", end="")
        else:
            print(" ", end="")
    print()  # New line after each row
