"""
给你二叉树的根结点 root ，请你将它展开为一个单链表：

展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 null 。
展开后的单链表应该与二叉树 先序遍历 顺序相同。
 

示例 1：


输入：root = [1,2,5,3,4,null,6]
输出：[1,null,2,null,3,null,4,null,5,null,6]
示例 2：

输入：root = []
输出：[]
示例 3：

输入：root = [0]
输出：[0]
 

提示：

树中结点数在范围 [0, 2000] 内
-100 <= Node.val <= 100
 

进阶：你可以使用原地算法（O(1) 额外空间）展开这棵树吗？

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/flatten-binary-tree-to-linked-list
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Utils.tree import TreeNode, Tree


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return
        new_root = TreeNode()
        last_ptr = new_root
        stack: List[TreeNode] = [root]
        while len(stack) > 0:
            current: TreeNode = stack.pop()
            print("current: {}".format(current.val))
            last_ptr.right = current
            last_ptr = current
            while last_ptr is not None:
                print("ptr: {}".format(last_ptr.val))
                if last_ptr.right is not None:
                    stack.append(last_ptr.right)
                if last_ptr.left is not None:
                    last_ptr.right = last_ptr.left
                    last_ptr.left = None
                    last_ptr = last_ptr.right
                elif last_ptr.left is None and last_ptr.right is None:
                    break


if __name__ == '__main__':
    t = Tree([1, 2, 5, 3, 4, 6, 7])
    Solution().flatten(t.root)
    ptr = t.root
    while ptr is not None:
        print(ptr.val)
        ptr = ptr.right
