n = int(input())

sequence = [int(input()) for _ in range(n)]
current = 1
stack = []
result = []

for num in sequence:
    while current <= num:
        stack.append(current)
        result.append("+")
        current += 1

    if stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        break
else:
    print("\n".join(result))
