# Function to print alphabet C
def print_C():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'C'
            if (j == 0) or (i == 0 and j != cols - 1) or (i == rows - 1 and j != cols - 1):  # Left vertical line and top/bottom horizontal lines
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'C'
print_C()
