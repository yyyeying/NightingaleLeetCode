"""
给你一个整数 n ，请你生成并返回所有由 n 个节点组成且节点值从 1 到 n 互不相同的不同 二叉搜索树 。可以按 任意顺序 返回答案。

 

示例 1：


输入：n = 3
输出：[[1,null,2,null,3],[1,null,3,2],[2,1,3],[3,1,null,null,2],[3,2,null,1]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 8

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/unique-binary-search-trees-ii
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
    def generateTrees(self, n: int) -> List[TreeNode]:

        def backtrack(start: int, end: int)->List[TreeNode]:
            trees = []
            if start > end:
                return [None]
            for i in range(start, end + 1):
                left_trees = backtrack(start, i - 1)
                right_trees = backtrack(i + 1, end)
                for l in left_trees:
                    for r in right_trees:
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        trees.append(root)
            return trees

        return backtrack(1, n) if n else []


if __name__ == '__main__':
    result = Solution().generateTrees(3)
