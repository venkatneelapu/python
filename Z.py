def print_alphabet_Z(N):
    # First row: N stars
    print('* ' * N)
    
    # Middle rows: stars at the diagonal (from top-right to bottom-left)
    for i in range(1, N-1):
        print('  ' * (N - i - 1) + '*')
    
    # Last row: N stars
    print('* ' * N)

# Input
N = int(input("Enter the size of the Z: "))
print_alphabet_Z(N)
