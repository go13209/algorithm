def solution(numbers, direction):
    answer = []
    if direction == 'right':
        answer.append(numbers.pop())
        for num in numbers:
            answer.append(num)
    else:
        for num in numbers[1:]:
            answer.append(num)
        answer.append(numbers[0])
    return answer