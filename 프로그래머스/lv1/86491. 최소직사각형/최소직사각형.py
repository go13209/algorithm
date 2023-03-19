def solution(sizes):
    x = []
    y = []
    
    for i in range(len(sizes)):
        w, h = sizes[i]

        if w > h:
            x.append(h)
            y.append(w)
        else:
            x.append(w)
            y.append(h)

    return max(x) * max(y)