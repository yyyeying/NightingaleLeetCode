# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

"""
给你一个链表，两两交换其中相邻的节点，并返回交换后链表的头节点。你必须在不修改节点内部的值的情况下完成本题（即，只能进行节点交换）。

 

示例 1：


输入：head = [1,2,3,4]
输出：[2,1,4,3]
示例 2：

输入：head = []
输出：[]
示例 3：

输入：head = [1]
输出：[1]
 

提示：

链表中节点的数目在范围 [0, 100] 内
0 <= Node.val <= 100
通过次数459,595提交次数647,774

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/swap-nodes-in-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from Utils.list import ListNode, construct_list, traverse


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        pre = ListNode()
        pre.next = head
        ptr = pre
        while ptr.next is not None and ptr.next.next is not None:
            previous = ptr
            a = previous.next
            b = a.next
            c = b.next
            previous.next = b
            b.next = a
            a.next = c
            ptr = a
        return pre.next


if __name__ == '__main__':
    s = Solution()
    my_list = construct_list([1])
    result = s.swapPairs(my_list)
    print(traverse(result))
