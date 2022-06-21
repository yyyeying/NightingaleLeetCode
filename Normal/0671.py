"""
给定一个非空特殊的二叉树，每个节点都是正数，并且每个节点的子节点数量只能为2或0。如果一个节点有两个子节点的话，那么该节点的值等于两个子节点中较小的一个。

更正式地说，root.val = min(root.left.val, root.right.val) 总成立。

给出这样的一个二叉树，你需要输出所有节点中的第二小的值。如果第二小的值不存在的话，输出 -1 。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/second-minimum-node-in-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree(nodes: List[int]):
    """
    题目没有告诉我他怎么用一个list建的这棵树，为了本地调试只能自己实现一个。
    :param nodes:
    :return:
    """
    count = 1
    layer_count = 1
    root = TreeNode(val=nodes[0])
    node_queue = [root]
    node_to_insert = None
    while count < len(nodes):
        layer_count *= 2
        # print('{}, {}'.format(count+layer_count, len(nodes)))
        candidate_nodes = nodes[count:min(count+layer_count, count+len(nodes))]
        candidate_nodes += [None for i in range(count+layer_count - len(nodes))]
        # print(candidate_nodes)
        for i in range(layer_count):
            # print("count: {}, layer count: {}, i: {}, node: {}".format(count, layer_count, i, candidate_nodes[i]))
            new_node = TreeNode(candidate_nodes[i])
            node_queue.insert(0, new_node)
            if not node_to_insert:
                node_to_insert = node_queue.pop()
            if not node_to_insert.left:
                node_to_insert.left = new_node
            else:
                node_to_insert.right = new_node
                if candidate_nodes[i] is None:
                    node_to_insert.left = None
                    node_to_insert.right = None
                node_to_insert = None
        count += layer_count
    return root


class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        node_stack = [root]
        result = 2 ** 31
        # print(result)
        while node_stack:
            # print([node.val for node in node_stack])
            node = node_stack.pop()
            if node.left:
                # print('{}, {}'.format(node.left.val, node.right.val))
                if result > node.left.val > node.val:
                    result = min(result, node.left.val)
                elif result > node.right.val > node.val:
                    result = min(result, node.right.val)
                node_stack.append(node.left)
                node_stack.append(node.right)
        if result < 2 ** 31:
            return result
        else:
            return -1


if __name__ == '__main__':
    nodes = [1, 1, 3, 1, 1, 3, 4, 3, 1, 1, 1, 3, 8, 4, 8, 3, 3, 1, 6, 2, 1]
    root = construct_tree(nodes)
    solution = Solution()
    result = solution.findSecondMinimumValue(root)
    print(result)
