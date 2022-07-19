from typing import List, Union, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self, list_: Optional[List[Union[int]]] = None, head: Optional[ListNode] = None):
        self.head = None
        if list_ is not None:
            self.construct(list_)
        elif head is not None:
            self.head = head

    def construct(self, list_: List[Union[int]]):
        # print("construct {}".format(list_))
        prev = ListNode()
        ptr = prev
        for i in list_:
            # print("new node {}".format(i))
            ptr.next = ListNode(val=i)
            ptr = ptr.next
        # print(prev.next.val)
        self.head = prev.next

    def traverse(self) -> List[Union[int]]:
        result = []
        ptr = self.head
        while ptr is not None:
            # print("value: {}".format(ptr.val))
            result.append(ptr.val)
            ptr = ptr.next
        return result
