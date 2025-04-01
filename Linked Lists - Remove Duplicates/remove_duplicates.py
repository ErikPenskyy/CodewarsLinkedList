def remove_duplicates(head):
    if head is None:
        return None
    curr = head
    while curr.next is not None:
        if curr.data == curr.next.data:
            curr.next = curr.next.next
        else:
            curr = curr.next
    return head
