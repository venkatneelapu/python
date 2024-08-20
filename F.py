# Function to print alphabet F
def print_F():
    rows = 7
    cols = 5
    for i in range(rows):
        for j in range(cols):
            # Conditions for the pattern of 'F'
            if j == 0:  # Left vertical line of 'F'
                print("*", end="")
            elif i == 0 or i == rows // 2:  # Top and middle horizontal lines
                print("*", end="")
            else:
                print(" ", end="")
        print()  # Move to the next line

# Call the function to print 'F'
print_F()
