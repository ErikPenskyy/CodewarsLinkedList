def swap_pairs(head):
    if head is None or head.next is None:
        return head
    prev_curr = Node(next=head)
    curr = prev_curr

    while curr.next and curr.next.next:
        head_1skip = curr.next
        head_2skip = curr.next.next
        head_1skip.next = head_2skip.next
        head_2skip.next = head_1skip
        curr.next = head_2skip
        curr = head_1skip

    return prev_curr.next
