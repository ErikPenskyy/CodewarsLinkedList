def stringify(node: Node):
    string = ''
    curr = node
    while curr is not None:
        string += str(curr.data) + ' -> '
        curr = curr.next
    string += 'None'
    return string
