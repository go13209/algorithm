N, M = map(int, input().split())

not_hear = set([input() for _ in range(N)])
not_see = set([input() for _ in range(M)])

intersection = sorted(not_hear & not_see)
print(len(intersection), *intersection, sep='\n')