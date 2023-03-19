def solution(brown, yellow):
    carpet = brown + yellow

    for h in range(1, yellow + 1):
        if yellow % h == 0:
            w = yellow // h

            if h > w:
                break

            carpet_width = w + 2
            carpet_height = h + 2

            if carpet_width * carpet_height - yellow == brown:
                return [carpet_width, carpet_height]