from typing import List


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def construct_tree(nodes: List[int], debug=False):
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
        if debug:
            print('count+layer_count: {}, nodes: {}'.format(count+layer_count, len(nodes)))
        candidate_nodes = nodes[count:min(count+layer_count, count+len(nodes))]
        candidate_nodes += [None for i in range(count+layer_count - len(nodes))]
        if debug:
            print('candidate nodes: {}'.format(candidate_nodes))
        for i in range(layer_count):
            if debug:
                print("count: {}, layer count: {}, i: {}, node: {}".format(count, layer_count, i, candidate_nodes[i]))
            new_node = TreeNode(candidate_nodes[i])
            node_queue.insert(0, new_node)
            if not node_to_insert:
                node_to_insert = node_queue.pop()
            if not node_to_insert.left:
                node_to_insert.left = new_node
            else:
                node_to_insert.right = new_node
                '''
                if candidate_nodes[i] is None:
                    node_to_insert.left = None
                    node_to_insert.right = None
                    '''
                node_to_insert = None
        count += layer_count
    return root