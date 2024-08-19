# Function to print alphabet E
def print_E():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'E'
            if j == 0:  # Left vertical line of 'E'
                print("*", end="")
            elif (i == 0 or i == rows // 2 or i == rows - 1):  # Top, middle, and bottom horizontal lines
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'E'
print_E()
