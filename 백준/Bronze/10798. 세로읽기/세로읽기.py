str = [[char for char in input()] for _ in range(5)]
max_len = 0
for s in str:
    if len(s) > max_len:
        max_len = len(s)
for i in range(max_len):
    for j in range(len(str)):
        try:
            print(str[j][i], end='')
        except:
            continue