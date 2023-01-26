N = int(input())
number_list = [n for n in range(1, N+1)]
discard = []

while len(number_list) > 1:
    print(number_list.pop(0), end=' ')
    number_list.append(number_list.pop(0))
    
print(number_list[0])