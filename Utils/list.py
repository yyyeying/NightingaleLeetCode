class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def construct_list(l: list) -> ListNode:
    nodes = []
    for i in range(len(l)):
        node = ListNode(l[i])
        if i > 0:
            nodes[i - 1].next = node
        nodes.append(node)
    return nodes[0]


def traverse(head: ListNode) -> list:
    result = []
    while head.next is not None:
        result.append(head.val)
        head = head.next
    result.append(head.val)
    return result
