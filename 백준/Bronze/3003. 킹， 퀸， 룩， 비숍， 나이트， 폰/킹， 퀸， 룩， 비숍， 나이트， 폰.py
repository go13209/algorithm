num = (input().split())
dict = {
    'king' : 1 - int(num[0]),
    'queen' : 1 - int(num[1]),
    'rook' : 2 - int(num[2]),
    'bishop' : 2 - int(num[3]),
    'knight' : 2 - int(num[4]),
    'pawn' : 8 - int(num[5]),
}
for i in dict.values():
    print(i, end=' ')