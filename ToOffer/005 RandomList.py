"""
请实现 copyRandomList 函数，复制一个复杂链表。在复杂链表中，每个节点除了有一个 next 指针指向下一个节点，还有一个 random 指针指向链表中的任意节点或者 null。

 

示例 1：



输入：head = [[7,null],[13,0],[11,4],[10,2],[1,0]]
输出：[[7,null],[13,0],[11,4],[10,2],[1,0]]
示例 2：



输入：head = [[1,1],[2,1]]
输出：[[1,1],[2,1]]
示例 3：



输入：head = [[3,null],[3,0],[3,null]]
输出：[[3,null],[3,0],[3,null]]
示例 4：

输入：head = []
输出：[]
解释：给定的链表为空（空指针），因此返回 null。
 

提示：

-10000 <= Node.val <= 10000
Node.random 为空（null）或指向链表中的节点。
节点数目不超过 1000 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        ptr = head
        new_head = None
        new_ptr = None
        head_constructed = False
        mapping = {}
        while ptr:
            new_node = Node(ptr.val)
            if head_constructed is False:
                new_head = new_node
                new_ptr = new_node
            else:
                new_ptr.next = new_node
            mapping.update({ptr: new_node})
            ptr = ptr.next
            if head_constructed is False:
                head_constructed = True
            else:
                new_ptr = new_ptr.next
        ptr = head
        new_ptr = new_head
        while new_ptr:
            if ptr.random is None:
                new_ptr.random = None
            else:
                new_ptr.random = mapping[ptr.random]
            new_ptr = new_ptr.next
            ptr = ptr.next
        return new_head

    def copyRandomList2(self, head: 'Node') -> 'Node':
        if head is None:
            return None
        current = head
        while current:
            new_node = Node(current.val)
            new_node.next = current.next
            current.next = new_node
            current = new_node.next
        current = head
        while current:
            if current.random:
                current.next.random = current.random.next
            current = current.next.next
        current = head
        new_head = current.next
        copy = head.next
        while current:
            current.next = current.next.next
            current = current.next
            if copy.next:
                copy.next = copy.next.next
            copy = copy.next
        return new_head