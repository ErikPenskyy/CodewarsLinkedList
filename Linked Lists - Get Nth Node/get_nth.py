def get_nth(node, index):
    curr = node
    length = 0
    while curr is not None:
        length += 1
        curr = curr.next
    curr = node
    if 0 <= index < length and curr.data is not None:
        for _ in range(index):
            curr = curr.next
        return curr
    raise AssertionError
