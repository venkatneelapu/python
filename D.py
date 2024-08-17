# Function to print alphabet D
def print_D():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'D'
            if j == 0:  # Left vertical line of 'D'
                print("*", end="")
            elif j == cols - 1 and (i != 0 and i != rows - 1):  # Right vertical line of 'D'
                print("*", end="")
            elif (i == 0 or i == rows - 1) and j != cols - 1:  # Top and bottom horizontal lines
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'D'
print_D()
