from typing import List, Union


class TreeNode:
    """
    Definition for a binary tree node.
    """

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Tree:
    def __init__(self, nodes: List[int], debug=False):
        """
        题目没有告诉我他怎么用一个list建的这棵树，为了本地调试只能自己实现一个。
        :param debug:
        :param nodes:
        :return:
        """
        count = 1
        layer_count = 1
        self.root = TreeNode(val=nodes[0])
        node_queue = [self.root]
        node_to_insert = None
        while count < len(nodes):
            layer_count *= 2
            if debug:
                print('count+layer_count: {}, nodes: {}'.format(count + layer_count, len(nodes)))
            candidate_nodes = nodes[count:min(count + layer_count, count + len(nodes))]
            candidate_nodes += [None for i in range(count + layer_count - len(nodes))]
            if debug:
                print('candidate nodes: {}'.format(candidate_nodes))
            for i in range(layer_count):
                if debug:
                    print(
                        "count: {}, layer count: {}, i: {}, node: {}".format(count, layer_count, i, candidate_nodes[i]))
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

    def level_order(self) -> List[List[int]]:
        """
        层序遍历
        :return:
        """
        result = []
        if self.root is None:
            return result
        queue: List[List[Union[TreeNode, int]]] = [[self.root, 0]]
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


