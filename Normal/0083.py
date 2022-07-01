"""
给定一个已排序的链表的头 head ， 删除所有重复的元素，使每个元素只出现一次 。返回 已排序的链表 。

 

示例 1：


输入：head = [1,1,2]
输出：[1,2]
示例 2：


输入：head = [1,1,2,3,3]
输出：[1,2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序 排列

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Utils.list import ListNode, construct_list, traverse


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        new_head = ListNode()
        new_head.next = head
        ptr = head
        pre = new_head
        while ptr.next is not None:
            # print(pre.val, ptr.val, ptr.next.val)
            if ptr.val == ptr.next.val:
                pre.next = ptr.next
            else:
                pre = pre.next
            ptr = ptr.next
        return new_head.next


if __name__ == '__main__':
    s = Solution()
    print(traverse(s.deleteDuplicates(construct_list([1, 1, 2, 3, 3]))))
