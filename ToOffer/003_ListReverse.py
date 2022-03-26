"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/cong-wei-dao-tou-da-yin-lian-biao-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for singly-linked list.
from typing import List


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def construct(self, l: List[int]) ->ListNode:
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

    def reversePrint(self, head: ListNode) -> List[int]:
        if head is None:
            return []
        a: ListNode = head
        count: int = 0
        while a:
            count += 1
            a = a.next
        result = [-1 for i in range(count)]
        ptr = head
        i = 0
        while ptr:
            result[count - i - 1] = ptr.val
            i += 1
            ptr = ptr.next
        return result


if __name__ == '__main__':
    s = Solution()
    head = s.construct([1, 3, 2])
    print(s.reversePrint(head))
    head = s.construct([])
    print(s.reversePrint(head))
