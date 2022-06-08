class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        return 0 if root is None else max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
