import sys

people = 0 ; max_people = 0

for _ in range(4):
    people_out, people_in = map(int, sys.stdin.readline().split())
    people += people_in - people_out
    if people > max_people:
        max_people = people

print(max_people)