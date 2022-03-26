"""
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。

 

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
 

限制：

0 <= 节点个数 <= 5000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fan-zhuan-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def construct(self, l: List[int]) -> ListNode:
        if len(l) > 0:
            head = ListNode(l[0])
            ptr = head
            for i in l[1:]:
                new_node = ListNode(i)
                ptr.next = new_node
                ptr = ptr.next
        else:
            head = None
        return head

    def traverse(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        result = []
        ptr = head
        while ptr:
            result.append(ptr.val)
            ptr = ptr.next
        return result

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        front: ListNode = head
        next: ListNode = None
        ptr: ListNode = None
        if front.next:
            next = front.next
            front.next = None
            while next:
                ptr = next.next
                next.next = front
                front = next
                next = ptr
        return front


if __name__ == '__main__':
    s = Solution()
    head = s.construct([1, 2, 3, 4, 5])
    print(s.traverse(head))
    tail = s.reverseList(head)
    print(s.traverse(tail))
