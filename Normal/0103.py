"""
给你二叉树的根节点 root ，返回其节点值的 锯齿形层序遍历 。（即先从左往右，再从右往左进行下一层遍历，以此类推，层与层之间交替进行）。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[20,9],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]
 

提示：

树中节点数目在范围 [0, 2000] 内
-100 <= Node.val <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-zigzag-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Union

from Utils.tree import TreeNode, Tree


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        result: List[List[int]] = []
        if root is None:
            return result
        queue: List[List[Union[TreeNode, int]]] = [[root, 0]]
        while len(queue) > 0:
            current = queue.pop()
            if len(result) <= current[1]:
                result.append([])
            if current[1] % 2 == 0:
                result[current[1]].append(current[0].val)
            else:
                result[current[1]].insert(0, current[0].val)
            if current[0].left is not None:
                queue.insert(0, [current[0].left, current[1] + 1])
            if current[0].right is not None:
                queue.insert(0, [current[0].right, current[1] + 1])

        return result


if __name__ == '__main__':
    t = Tree([3, 9, 20, None, None, 15, 7])
    result = Solution().zigzagLevelOrder(t.root)
    print(result)
