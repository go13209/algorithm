string = list(input())
t = int(input())

left_stack = string
right_stack = []

for _ in range(t):
    command = input().split()
    
    if command[0] == 'L':
        if left_stack:
            right_stack.append(left_stack.pop())
    
    elif command[0] == 'D':
        if right_stack:
            left_stack.append(right_stack.pop())
    
    elif command[0] == 'B':
        if left_stack:
            left_stack.pop()
    
    else:
        left_stack.append(command[1])

print(''.join(left_stack + right_stack[::-1]))