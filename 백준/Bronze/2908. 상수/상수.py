a, b = input().split()
new_a = ''
new_b = ''

for i in list(reversed(a)):
    new_a += i
for i in list(reversed(b)):
    new_b += i

if int(new_a) > int(new_b):
    print(int(new_a))
else:
    print(int(new_b))