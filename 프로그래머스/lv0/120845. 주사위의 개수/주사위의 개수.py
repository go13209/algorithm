def solution(box, n):
    length, width, height = box
    answer = (length//n) * (width//n) * (height//n)
    return answer