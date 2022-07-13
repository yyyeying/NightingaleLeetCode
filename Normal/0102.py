"""给你二叉树的根节点 root ，返回其节点值的 层序遍历 。 （即逐层地，从左到右访问所有节点）。

 

示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[3],[9,20],[15,7]]
示例 2：

输入：root = [1]
输出：[[1]]
示例 3：

输入：root = []
输出：[]
 

提示：

树中节点数目在范围 [0, 2000] 内
-1000 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/binary-tree-level-order-traversal
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import List, Union

from Utils.tree import TreeNode, Tree


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        result = []
        if root is None:
            return result
        queue: List[List[Union[TreeNode, int]]] = [[root, 0]]
        while len(queue) > 0:
            current = queue.pop()
            if len(result) <= current[1]:
                result.append([])
            result[current[1]].append(current[0].val)
            if current[0].left is not None:
                queue.insert(0, [current[0].left, current[1] + 1])
            if current[0].right is not None:
                queue.insert(0, [current[0].right, current[1] + 1])
        return result


if __name__ == '__main__':
    t = Tree([3, 9, 20, None, None, 15, 7])
    level_order = Solution().levelOrder(t.root)
    print(level_order)
