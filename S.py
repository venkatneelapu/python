# Function to print alphabet S
def print_S():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'S'
            if (i == 0 or i == rows // 2 or i == rows - 1):  # Top, middle, and bottom horizontal lines
                print("*", end="")
            elif i < rows // 2 and j == 0:  # Vertical line on the left for the top half of 'S'
                print("*", end="")
            elif i > rows // 2 and j == cols - 1:  # Vertical line on the right for the bottom half of 'S'
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'S'
print_S()
