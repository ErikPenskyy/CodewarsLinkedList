def sorted_insert(head, data):
    list_of_prev = []
    if head is None:
        return Node(data)
    while head is not None:
        if head.data <= data:
            list_of_prev.append(head.data)
            head = head.next
        else:
            break
    sorted_node = Node(data)
    sorted_node.next = head

    for elem in list_of_prev[::-1]:
        sorted_node_1 = Node(elem)
        sorted_node_1.next = sorted_node
        sorted_node = sorted_node_1
    return sorted_node
