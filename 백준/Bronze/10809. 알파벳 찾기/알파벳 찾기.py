alphabet_dict = {}
for n in range(97, 123):
    alphabet_dict[chr(n)] = n - 97
input_list = list(map(str, input()))
for a in alphabet_dict.keys():
    if a in input_list:
        print(input_list.index(a), end = ' ')
    else:
        print(-1, end=' ')