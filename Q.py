# Function to print alphabet Q
def print_Q():
    rows = 7
    cols = 7
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'Q'
            if (i == 0 or i == rows - 1) and (j > 0 and j < cols - 1):  # Top and bottom horizontal lines
                print("*", end="")
            elif (j == 0 or j == cols - 1) and (i > 0 and i < rows - 1):  # Left and right vertical lines
                print("*", end="")
            elif i == rows - 2 and j == cols - 2:  # Diagonal line of 'Q'
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'Q'
print_Q()
