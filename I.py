def print_I():
    for row in range(7):  # Height of the letter
        if row == 0 or row == 6:
            print("*****")  # Top and bottom of the "I"
        else:
            print("  *  ")  # Middle part of the "I"

print_I()