# Function to print alphabet R
def print_R():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'R'
            if j == 0:  # Left vertical line of 'R'
                print("*", end="")
            elif (i == 0 or i == rows // 2) and j < cols - 1:  # Top and middle horizontal lines of 'R'
                print("*", end="")
            elif j == cols - 1 and i != 0 and i < rows // 2:  # Right vertical line in the top half of 'R'
                print("*", end="")
            elif i == j + rows // 2:  # Diagonal line in the bottom half of 'R'
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'R'
print_R()
