def reverse(head):
    if head is None:
        return None
    list_of_nodes = []
    while head is not None:
        list_of_nodes.append(head.data)
        head = head.next

    curr = Node(list_of_nodes[0])
    for _, linked in enumerate(list_of_nodes[1:]):
        next_val = Node(linked)
        next_val.next = curr
        curr = next_val
    return curr
