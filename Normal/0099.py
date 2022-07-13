"""
给你二叉搜索树的根节点 root ，该树中的 恰好 两个节点的值被错误地交换。请在不改变其结构的情况下，恢复这棵树 。

 

示例 1：


输入：root = [1,3,null,null,2]
输出：[3,1,null,null,2]
解释：3 不能是 1 的左孩子，因为 3 > 1 。交换 1 和 3 使二叉搜索树有效。
示例 2：


输入：root = [3,1,4,null,null,2]
输出：[2,1,4,null,null,3]
解释：2 不能在 3 的右子树中，因为 2 < 3 。交换 2 和 3 使二叉搜索树有效。
 

提示：

树上节点的数目在范围 [2, 1000] 内
-231 <= Node.val <= 231 - 1
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/recover-binary-search-tree
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
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        stack: List[TreeNode] = [root]
        pre: TreeNode = None
        x: TreeNode = None
        y: TreeNode = None
        while len(stack) > 0 and root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            root: TreeNode = stack.pop()
            print("root.val = {}".format(root.val))
            if pre is not None and root.val < pre.val:
                y = root
                if x is None:
                    x = pre
                else:
                    break
            pre = root
            root = root.right
        x.val, y.val = y.val, x.val


if __name__ == '__main__':
    t = Tree([1, 3, None, None, 2])
    Solution().recoverTree(t.root)

