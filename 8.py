# Number of rows for the height of the "8"
rows = 7

for i in range(1, rows + 1):
    if i == 1 or i == rows or i == rows // 2 + 1:
        print('*' * rows)  # Top, middle, and bottom horizontal lines
    else:
        print('*' + ' ' * (rows - 2) + '*')  # Vertical lines on both sides
