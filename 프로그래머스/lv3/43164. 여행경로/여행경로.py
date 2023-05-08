def solution(tickets):
    ticket_dict = {}
    for depart, arrive in tickets:
        if depart not in ticket_dict:
            ticket_dict[depart] = [arrive]
        else:
            ticket_dict[depart].append(arrive)
            ticket_dict[depart].sort()

    stack = ["ICN"]
    path = []

    while stack:
        current = stack[-1]
        if current in ticket_dict and ticket_dict[current]:
            stack.append(ticket_dict[current].pop(0))
        else:
            path.append(stack.pop())

    return path[::-1]