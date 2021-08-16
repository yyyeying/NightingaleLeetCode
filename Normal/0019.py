from Utils.list import ListNode, construct_list, traverse


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast = head
        slow = head
        for i in range(n - 1):
            fast = fast.next
            print(fast.val)
        if head.next is None and n == 1:
            return None
        formal = None
        while fast.next is not None:
            formal = slow
            slow = slow.next
            fast = fast.next
        next_temp = slow.next
        if formal is not None:
            formal.next = next_temp
        else:
            head = next_temp
        return head


if __name__ == '__main__':
    nodes = [1, 2]
    head = construct_list(nodes)
    print(traverse(head))
    s = Solution()
    head = s.removeNthFromEnd(head, 2)
    print(traverse(head))
