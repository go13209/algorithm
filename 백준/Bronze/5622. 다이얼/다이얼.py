dial_dict = {
    'ABC': 3,
    'DEF': 4,
    'GHI': 5,
    'JKL': 6,
    'MNO': 7,
    'PQRS': 8,
    'TUV': 9,
    'WXYZ': 10,
    '0': 11
}

str = input()
total = 0
for key in dial_dict.keys():
    for char in str:
        if char in key:
            total += dial_dict[key]
print(total)