"""
给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。

插入排序 算法的步骤:

插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。
每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。
重复直到所有输入数据插入完为止。
下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表中。

对链表进行插入排序。



 

示例 1：



输入: head = [4,2,1,3]
输出: [1,2,3,4]
示例 2：



输入: head = [-1,5,3,4,0]
输出: [-1,0,3,4,5]
 

提示：

列表中的节点数在 [1, 5000]范围内
-5000 <= Node.val <= 5000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/insertion-sort-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
from Utils.list import ListNode, LinkedList


class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        new_head = ListNode(-5001, head)
        prev = new_head
        current = head
        while current is not None:
            print("current: {}".format(current.val))
            t = current.next
            ptr = new_head
            changed = False
            while ptr != current:
                if ptr.val <= current.val < ptr.next.val:
                    print("insert {} into {}.next".format(current.val, ptr.val))
                    prev.next = current.next
                    temp = ptr.next
                    ptr.next = current
                    current.next = temp
                    current = t
                    changed = True
                    break
                ptr = ptr.next
            if changed is False:
                prev = prev.next
                current = current.next
        return new_head.next


if __name__ == '__main__':
    l = LinkedList([1, 4, 3, 5, 2])
    result = Solution().insertionSortList(l.head)
    print(LinkedList(head=result).traverse())
    l = LinkedList([4, 2, 1, 3])
    result = Solution().insertionSortList(l.head)
    print(LinkedList(head=result).traverse())
    l = LinkedList([4, 19, 14, 5, -3, 1, 8, 5, 11, 15])
    result = Solution().insertionSortList(l.head)
    print(LinkedList(head=result).traverse())

