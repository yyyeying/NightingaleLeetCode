"""
给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。

你应当 保留 两个分区中每个节点的初始相对位置。

 

示例 1：


输入：head = [1,4,3,2,5,2], x = 3
输出：[1,2,2,4,3,5]
示例 2：

输入：head = [2,1], x = 2
输出：[1,2]
 

提示：

链表中节点的数目在范围 [0, 200] 内
-100 <= Node.val <= 100
-200 <= x <= 200

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/partition-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Utils.list import ListNode, construct_list, traverse


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        new_head = ListNode()
        new_head.next = head
        low_ptr = new_head
        ptr = head
        pre = new_head
        while ptr is not None:
            # print("pre = {}, ptr = {}, low_ptr = {}".format(pre.val, ptr.val, low_ptr.val))
            if ptr.val < x:
                if low_ptr.next == ptr:
                    low_ptr = low_ptr.next
                    pre = pre.next
                    ptr = ptr.next
                else:
                    temp = ptr.next
                    pre.next = ptr.next
                    low_temp = low_ptr.next
                    low_ptr.next = ptr
                    low_ptr = ptr
                    ptr.next = low_temp
                    ptr = temp
            else:
                ptr = ptr.next
                pre = pre.next
        return new_head.next


if __name__ == '__main__':
    s = Solution()
    result = s.partition(construct_list([1, 4, 3, 2, 5, 2]), 3)
    print(traverse(result))
    result = s.partition(construct_list([2, 1]), 2)
    print(traverse(result))
