"""
给定一个单链表 L 的头节点 head ，单链表 L 表示为：

L0 → L1 → … → Ln - 1 → Ln
请将其重新排列后变为：

L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

 

示例 1：



输入：head = [1,2,3,4]
输出：[1,4,2,3]
示例 2：



输入：head = [1,2,3,4,5]
输出：[1,5,2,4,3]
 

提示：

链表的长度范围为 [1, 5 * 104]
1 <= node.val <= 1000
通过次数195,166提交次数304,584

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reorder-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Utils.list import ListNode, LinkedList


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return
        ptr: ListNode = head
        nodes = {}
        i = 0
        while ptr is not None:
            nodes.update({i: ptr})
            i += 1
            ptr = ptr.next
        # ptr = head
        new_head = ListNode()
        temp = new_head
        # print("total node {}".format(i))
        for j in range(int((i - 1) / 2) + 1):
            # print("append node {}".format(j))
            ptr = nodes[j]
            temp.next = ptr
            if i - j - 1 == j:
                ptr.next = None
            else:
                # print("append node {}".format(i - j - 1))
                ptr.next = nodes[i - j - 1]
                temp = ptr.next
                if j == int((i - 1) / 2):
                    temp.next = None
        # head = new_head.next
        # print("finish")


if __name__ == '__main__':
    list_ = LinkedList([0, 1, 2, 3, 4])
    print(list_.traverse())
    # print(list_.head)
    Solution().reorderList(list_.head)
    print(list_.traverse())
    list_ = LinkedList([0, 1, 2, 3])
    print(list_.traverse())
    # print(list_.head)
    Solution().reorderList(list_.head)
    print(list_.traverse())
