"""
给你一个链表的头节点 head ，旋转链表，将链表每个节点向右移动 k 个位置。

 

示例 1：


输入：head = [1,2,3,4,5], k = 2
输出：[4,5,1,2,3]
示例 2：


输入：head = [0,1,2], k = 4
输出：[2,0,1]
 

提示：

链表中节点的数目在范围 [0, 500] 内
-100 <= Node.val <= 100
0 <= k <= 2 * 109

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/rotate-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from typing import Optional

from Utils.list import ListNode, construct_list, traverse


class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if head is None:
            return None
        n = 1
        ptr = head
        while ptr.next is not None:
            ptr = ptr.next
            n += 1
        if k % n == 0:
            return head
        last = head
        for i in range(k % n - 1):
            last = last.next
            if last is None:
                last = head
        # print(last.val)
        new_head = head
        new_tail = head
        i = 0
        while last.next is not None:
            # print(new_head.val)
            last = last.next
            new_head = new_head.next
            if i > 0:
                new_tail = new_tail.next
            i += 1
        last.next = head
        new_tail.next = None
        return new_head


if __name__ == '__main__':
    s = Solution()
    head = construct_list([1, 2])
    new_head = s.rotateRight(head, 2)
    print(new_head.val)
    print(traverse(new_head))
