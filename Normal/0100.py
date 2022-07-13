"""
给你两棵二叉树的根节点 p 和 q ，编写一个函数来检验这两棵树是否相同。

如果两个树在结构上相同，并且节点具有相同的值，则认为它们是相同的。

 

示例 1：


输入：p = [1,2,3], q = [1,2,3]
输出：true
示例 2：


输入：p = [1,2], q = [1,null,2]
输出：false
示例 3：


输入：p = [1,2,1], q = [1,1,2]
输出：false
 

提示：

两棵树上的节点数目都在范围 [0, 100] 内
-104 <= Node.val <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/same-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List

from Utils.tree import TreeNode


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p is None and q is None:
            return True
        quque1: List[TreeNode] = [p]
        queue2: List[TreeNode] = [q]
        while len(quque1) > 0 or len(queue2) > 0:
            if len(quque1) == 0 or len(queue2) == 0:
                return False
            current1 = quque1.pop()
            current2 = queue2.pop()
            if (current1 is None and current2 is not None) or (current2 is None and current1 is not None):
                return False
            if current1.val != current2.val:
                return False
            if current1.left is not None:
                if current2.left is None:
                    return False
                quque1.insert(0, current1.left)
                queue2.insert(0, current2.left)
            else:
                if current2.left is not None:
                    return False
            if current1.right is not None:
                if current2.right is None:
                    return False
                quque1.insert(0, current1.right)
                queue2.insert(0, current2.right)
            else:
                if current2.right is not None:
                    return False
        return True
