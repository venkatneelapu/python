# Function to print alphabet K
def print_K():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'K'
            if j == 0:  # Left vertical line of 'K'
                print("*", end="")
            elif j == rows - i - 1 and i <= rows // 2:  # Diagonal line from top-left to middle
                print("*", end="")
            elif j == i - rows // 2 and i > rows // 2:  # Diagonal line from middle to bottom-left
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'K'
print_K()
