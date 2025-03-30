def linked_list_from_string(s):
    list_of_linked = s.split(' -> ')[::-1]
    if len(list_of_linked) == 1:
        return None
    curr = Node(list_of_linked[1])
    for _, linked in enumerate(list_of_linked[2:]):
        next_val = Node(linked, curr)
        curr = next_val
    return curr
