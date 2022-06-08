from Utils.tree import TreeNode


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        # print(self.depth(root.left))
        # print(self.depth(root.right))
        if root is None:
            return True
        if abs(self.depth(root.left) - self.depth(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def depth(self, root: TreeNode) -> int:
        return 0 if root is None else max(self.depth(root.left), self.depth(root.right))+1
