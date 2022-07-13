"""
给你一个二叉树的根节点 root ， 检查它是否轴对称。

 

示例 1：


输入：root = [1,2,2,3,4,4,3]
输出：true
示例 2：


输入：root = [1,2,2,null,3,null,3]
输出：false
 

提示：

树中节点数目在范围 [1, 1000] 内
-100 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/symmetric-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

from Utils.tree import TreeNode, Tree


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue_left: List[TreeNode] = []
        queue_right: List[TreeNode] = []
        if root.left is not None and root.right is not None:
            queue_left.insert(0, root.left)
            queue_right.insert(0, root.right)
        elif root.left is None and root.right is None:
            return True
        else:
            return False
        while len(queue_left) > 0 or len(queue_right) > 0:
            if len(queue_left) == 0 or len(queue_right) == 0:
                return False
            left = queue_left.pop()
            right = queue_right.pop()
            # print("left: {}, right:{}".format(left.val, right.val))
            if left.val != right.val:
                return False
            if left.left is not None:
                if right.right is None:
                    return False
                queue_left.insert(0, left.left)
                queue_right.insert(0, right.right)
            elif right.right is not None:
                return False
            if left.right is not None:
                if right.left is None:
                    return False
                queue_left.insert(0, left.right)
                queue_right.insert(0, right.left)
            elif right.left is not None:
                return False
        return True


if __name__ == '__main__':
    t = Tree([1, 2, 2, 3, 4, 4, 3])
    result = Solution().isSymmetric(t.root)
    print(result)
