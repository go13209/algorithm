str = input().upper()
dict = {}
most_used = []
for char in str:
    if char not in dict:
        dict[char] = 1
    else:
        dict[char] += 1
for key, value in dict.items():
    if value == max(dict.values()):
        most_used.append(key)
if len(most_used) > 1:
    print('?')
else:
    print(*most_used)