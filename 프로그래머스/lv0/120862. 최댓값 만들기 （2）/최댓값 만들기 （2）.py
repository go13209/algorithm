def solution(numbers):
    down_to_up = sorted(numbers)
    if down_to_up[0] * down_to_up[1] >= down_to_up[-1] * down_to_up[-2]:
        answer = down_to_up[0] * down_to_up[1]
    elif down_to_up[0] * down_to_up[1] <= down_to_up[-1] * down_to_up[-2]:
        answer = down_to_up[-1] * down_to_up[-2]
    return answer