dict = {
    (1, 2) : 'B',
    (1, 3) : 'A',
    (2, 1) : 'A',
    (2, 3) : 'B',
    (3, 1) : 'B',
    (3, 2) : 'A'
}
game = tuple(map(int, input().split()))
print(dict[game])