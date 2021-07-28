"""
给定一个二叉树（具有根结点root），一个目标结点target，和一个整数值 K 。

返回到目标结点 target 距离为 K 的所有结点的值的列表。 答案可以以任何顺序返回。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/all-nodes-distance-k-in-binary-tree
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
    node_list = [root]
    node_queue = [root]
    node_to_insert = None
    while count < len(nodes):
        layer_count *= 2
        # print('{}, {}'.format(count+layer_count, len(nodes)))
        candidate_nodes = nodes[count:min(count + layer_count, count + len(nodes))]
        candidate_nodes += [None for i in range(count + layer_count - len(nodes))]
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
            node_list.append(new_node)
        count += layer_count
    return root, node_list


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        node_stack = [{'node': target, 'step': k, 'visited': [target]}]
        result = []
        while len(node_stack) > 0:
            # print(node_stack)
            print([n['node'].val for n in node_stack])
            node = node_stack.pop()
            # print(node['node'].val)
            if node['step'] == 0:
                result.append(node['node'].val)
            else:
                if node != root:
                    parent = self.find_parent(root, node['node'])
                    if parent is not None:
                        if parent not in node['visited']:
                            node_stack.append({'node': parent, 'step': node['step'] - 1, 'visited': node['visited']+[parent]})
                if node['node'].left is not None:
                    left = node['node'].left
                    if left not in node['visited']:
                        node_stack.append({'node': left, 'step': node['step'] - 1, 'visited': node['visited']+[left]})
                if node['node'].right is not None:
                    right = node['node'].right
                    if right not in node['visited']:
                        node_stack.append({'node': right, 'step': node['step'] - 1, 'visited': node['visited']+[right]})
        return result

    def find_parent(self, root: TreeNode, target: TreeNode):
        """
        小节点找爸爸
        """
        # print(target)
        if target == root:
            return None
        node_stack = [root]
        while len(node_stack) > 0:
            # print('find parent: {}'.format([n.val for n in node_stack]))
            node = node_stack.pop()
            if node.left is not None:
                if node.left.val == target.val:
                    # print('parent is {}'.format(node.val))
                    return node
                else:
                    node_stack.append(node.left)
            if node.right is not None:
                if node.right.val == target.val:
                    # print('parent is {}'.format(node.val))
                    return node
                else:
                    node_stack.append(node.right)
        return None


if __name__ == '__main__':
    nodes = [3, 5, 1, 6, 2, 0, 8, None, None, 7, 4]
    root, node_list = construct_tree(nodes)
    print([node.val for node in node_list])
    solution = Solution()
    result = solution.distanceK(root, node_list[1], 2)
    print(result)
