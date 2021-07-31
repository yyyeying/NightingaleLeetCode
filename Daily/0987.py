"""
给你二叉树的根结点 root ，请你设计算法计算二叉树的 垂序遍历 序列。

对位于(row, col)的每个结点而言，其左右子结点分别位于(row + 1, col - 1)和(row + 1, col + 1) 。树的根结点位于 (0, 0) 。

二叉树的 垂序遍历 从最左边的列开始直到最右边的列结束，按列索引每一列上的所有结点，形成一个按出现位置从上到下排序的有序列表。
如果同行同列上有多个结点，则按结点的值从小到大进行排序。

返回二叉树的 垂序遍历 序列。


示例 1：


输入：root = [3,9,20,null,null,15,7]
输出：[[9],[3,15],[20],[7]]
解释：
列 -1 ：只有结点 9 在此列中。
列  0 ：只有结点 3 和 15 在此列中，按从上到下顺序。
列  1 ：只有结点 20 在此列中。
列  2 ：只有结点 7 在此列中。
示例 2：


输入：root = [1,2,3,4,5,6,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
列 -2 ：只有结点 4 在此列中。
列 -1 ：只有结点 2 在此列中。
列  0 ：结点 1 、5 和 6 都在此列中。
          1 在上面，所以它出现在前面。
          5 和 6 位置都是 (2, 0) ，所以按值从小到大排序，5 在 6 的前面。
列  1 ：只有结点 3 在此列中。
列  2 ：只有结点 7 在此列中。
示例 3：


输入：root = [1,2,3,4,6,5,7]
输出：[[4],[2],[1,5,6],[3],[7]]
解释：
这个示例实际上与示例 2 完全相同，只是结点 5 和 6 在树中的位置发生了交换。
因为 5 和 6 的位置仍然相同，所以答案保持不变，仍然按值从小到大排序。

提示：

树中结点数目总数在范围 [1, 1000] 内
0 <= Node.val <= 1000

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/vertical-order-traversal-of-a-binary-tree
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

from Utils.tree import TreeNode, construct_tree


class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        result = [[]]
        node_queue = [[root, [0, 0]]]
        max_position = 0
        min_position = 0
        while len(node_queue) > 0:
            node, position = node_queue.pop()
            print('node: [{}, {}]'.format(node.val, position))
            if position[1] < min_position:
                result.insert(0, [])
                min_position -= 1
            elif position[1] > max_position:
                result.append([])
                max_position += 1
            result[position[1] - min_position].append([node.val, position])
            print('result: {}'.format(result))
            if node.left and node.left.val is not None:
                print('left: {}'.format([node.left.val, [position[0] + 1, position[1] - 1]]))
                node_queue.insert(0, [node.left, [position[0] + 1, position[1] - 1]])
            if node.right and node.right.val is not None:
                print('right: {}'.format([node.right.val, [position[0] + 1, position[1] + 1]]))
                node_queue.insert(0, [node.right, [position[0] + 1, position[1] + 1]])
            print('node_queue: {}'.format([[n[0].val, n[1]] for n in node_queue]))
            result = [sorted(r, key=lambda x: (x[1][0], x[1][1], x[0])) for r in result]
        return [[y[0] for y in x] for x in result]


if __name__ == '__main__':
    null = None
    nodes = [1, 2, 3, 4, 6, 5, 7]
    tree = construct_tree(nodes, debug=True)
    solution = Solution()
    result = solution.verticalTraversal(tree)
    print(result)
