alphabet = [chr(i) for i in range(ord('A'), ord('Z') + 1)]
caesar = [chr(i) for i in range(ord('D'), ord('Z') + 1)] + ['A', 'B', 'C']

for char in list(input()):
    print(alphabet[caesar.index(char)], end='')