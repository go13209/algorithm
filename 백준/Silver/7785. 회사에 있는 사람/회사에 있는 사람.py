T = int(input())
inside = []
company = {}
for t in range(T):
    a, b = input().split()
    company[a] = b
for key in company.keys():
    if company[key] == 'enter':
        inside.append(key)
print(*sorted(inside, reverse=True), sep='\n')