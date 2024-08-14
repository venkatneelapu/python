# Function to print alphabet B
def print_B():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'B'
            if j == 0:  # Left vertical line of 'B'
                print("*", end="")
            elif (j == cols - 1 and (i != 0 and i != rows // 2 and i != rows - 1)) or \
                 ((i == 0 or i == rows // 2 or i == rows - 1) and j != cols - 1):  # Right vertical line and the horizontal lines
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'B'
print_B()
