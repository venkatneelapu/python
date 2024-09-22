# Number of rows
rows = 7

for i in range(1, rows + 1):
    if i <= 4:
        print('*' + ' ' * (rows - 3) + '*')  # Left and right vertical lines
    elif i == 5:
        print('*' * rows)  # Horizontal line
    else:
        print(' ' * (rows - 1) + '*')  # Right vertical line
