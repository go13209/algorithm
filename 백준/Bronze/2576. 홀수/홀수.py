dict = {
    'even' : [],
    'odd' : []
}
for i in range(7):
    number = int(input())
    if number % 2 == 0:
        dict['even'].append(number)
    else:
        dict['odd'].append(number)

if dict['odd'] == []:
    print(-1)
else:
    print(sum(dict['odd']), min(dict['odd']), sep='\n')