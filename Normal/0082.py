"""
给定一个已排序的链表的头 head ， 删除原始链表中所有重复数字的节点，只留下不同的数字 。返回 已排序的链表 。

 

示例 1：


输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]
示例 2：


输入：head = [1,1,1,2,3]
输出：[2,3]
 

提示：

链表中节点数目在范围 [0, 300] 内
-100 <= Node.val <= 100
题目数据保证链表已经按升序 排列

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/remove-duplicates-from-sorted-list-ii
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
        number: int = -101
        while ptr.next is not None:
            # print("ptr.val = {}, number = {}".format(ptr.val, number))
            if ptr.val == number or ptr.val == ptr.next.val:
                number = ptr.val
                pre.next = ptr.next
                ptr = ptr.next
            else:
                pre = ptr
                ptr = ptr.next
        if ptr.val == number:
            pre.next = ptr.next
        return new_head.next


if __name__ == '__main__':
    s = Solution()
    new_list = construct_list([1, 2, 3, 3, 4, 4, 5])
    result = s.deleteDuplicates(new_list)
    print(traverse(result))
    new_list = construct_list([1, 1, 1, 2, 5])
    result = s.deleteDuplicates(new_list)
    print(traverse(result))
    new_list = construct_list([1, 1])
    result = s.deleteDuplicates(new_list)
    print(traverse(result))
    new_list = construct_list([])
    result = s.deleteDuplicates(new_list)
    print(traverse(result))
