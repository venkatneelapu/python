def print_p():
    for row in range(7):
        for col in range(5):
            if col == 0 or (col == 4 and (row == 1 or row == 2)) or (row == 0 or row == 3):
                print("*", end="")
            else:
                print(" ", end="")
        print()

print_p()