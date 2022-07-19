"""给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。

 

示例 1：


输入：head = [4,2,1,3]
输出：[1,2,3,4]
示例 2：


输入：head = [-1,5,3,4,0]
输出：[-1,0,3,4,5]
示例 3：

输入：head = []
输出：[]
 

提示：

链表中节点的数目在范围 [0, 5 * 104] 内
-105 <= Node.val <= 105

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Utils.list import ListNode, LinkedList


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None
        # print("sort: {}".format(LinkedList(head=head).traverse()))
        if head.next is None:
            return head
        if head.next.next is None:
            if head.val <= head.next.val:
                return head
            else:
                new_head = head.next
                new_head.next = head
                head.next = None
                return new_head
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            fast = fast.next.next
            slow = slow.next
        b_head = slow.next
        slow.next = None
        # print("a: {}, b: {}".format(LinkedList(head=head).traverse(), LinkedList(head=b_head).traverse()))
        return self.combine(self.sortList(head), self.sortList(b_head))

    def combine(self, a: ListNode, b: ListNode) -> ListNode:
        # print("combine: a: {}, b: {}".format(LinkedList(head=a).traverse(), LinkedList(head=b).traverse()))
        new_head = ListNode()
        ptr = new_head
        ptr_a = a
        ptr_b = b
        while ptr_a is not None or ptr_b is not None:
            if ptr_a is None:
                ptr.next = ptr_b
                break
            elif ptr_b is None:
                ptr.next = ptr_a
                break
            if ptr_a.val < ptr_b.val:
                ptr.next = ptr_a
                ptr_a = ptr_a.next
                ptr = ptr.next
            else:
                ptr.next = ptr_b
                ptr_b = ptr_b.next
                ptr = ptr.next
        return new_head.next


if __name__ == '__main__':
    list_ = LinkedList([-1, 5, 3, 4, 0])
    result = LinkedList(head=Solution().sortList(list_.head))
    print(result.traverse())
