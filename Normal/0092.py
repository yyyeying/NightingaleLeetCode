"""
给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链表节点，返回 反转后的链表 。
 

示例 1：


输入：head = [1,2,3,4,5], left = 2, right = 4
输出：[1,4,3,2,5]
示例 2：

输入：head = [5], left = 1, right = 1
输出：[5]
 

提示：

链表中节点数目为 n
1 <= n <= 500
-500 <= Node.val <= 500
1 <= left <= right <= n

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/reverse-linked-list-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Utils.list import ListNode, construct_list, traverse


class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        new_head = ListNode()
        new_head.next = head
        pre = new_head
        left_ptr = head
        right_ptr = head
        for i in range(right - 1):
            if i < left - 1:
                left_ptr = left_ptr.next
                pre = pre.next
            right_ptr = right_ptr.next
        after = right_ptr.next
        # print("pre: {}, left: {}, right: {}".format(pre.val, left_ptr.val, right_ptr.val))
        ptr = left_ptr
        real_pre = pre
        for i in range(right - left + 1):
            temp = ptr.next
            ptr.next = real_pre
            real_pre = ptr
            ptr = temp
        left_ptr.next = after
        pre.next = right_ptr
        return new_head.next


if __name__ == '__main__':
    result = Solution().reverseBetween(construct_list([1, 2, 3, 4, 5]), 2, 4)
    print(traverse(result))
    result = Solution().reverseBetween(construct_list([5]), 1, 1)
    print(traverse(result))
