"""
存在一个由 n 个不同元素组成的整数数组 nums ，但你已经记不清具体内容。好在你还记得 nums 中的每一对相邻元素。

给你一个二维整数数组 adjacentPairs ，大小为 n - 1 ，其中每个 adjacentPairs[i] = [ui, vi] 表示元素 ui 和 vi 在 nums 中相邻。

题目数据保证所有由元素 nums[i] 和 nums[i+1] 组成的相邻元素对都存在于 adjacentPairs 中，存在形式可能是 [nums[i], nums[i+1]] ，也可能是 [nums[i+1], nums[i]] 。这些相邻元素对可以 按任意顺序 出现。

返回 原始数组 nums 。如果存在多种解答，返回 其中任意一个 即可。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/restore-the-array-from-adjacent-pairs
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Node:
    def __init__(self, number: int):
        # print("new node: {}".format(number))
        self.number = number
        self.links = []


class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        self.node_list = []
        result_list = []
        if len(adjacentPairs) == 1:
            return adjacentPairs[0]
        for link in adjacentPairs:
            self.handle_node(link)
        # print('nodes: {}'.format([node.number for node in self.node_list]))
        for node in self.node_list:
            if len(node.links) > 1:
                result_list = self.dfs(node)
                break
        return result_list

    def dfs(self, node: Node):
        result_list = [[node.number, node.links[0].number], [node.number, node.links[1].number]]
        nodes = [node.links[0], node.links[1]]
        for i in range(len(nodes)):
            while len(nodes[i].links) > 1:
                # print('current node: {}'.format(nodes[i].number))
                # print('links: '.format([adj.number for adj in nodes[i].links]))
                for n in nodes[i].links:
                    if n.number not in result_list[i]:
                        nodes[i] = n
                        result_list[i].append(n.number)
                    # print('result: {}'.format(result_list[i]))
        result_list[0].reverse()
        result_list[0].remove(result_list[0][-1])
        result = result_list[0] + result_list[1]
        return result

    def handle_node(self, link: List[int]):
        # print("link: {}".format(link))
        nodes = [None for i in range(len(link))]
        for node in self.node_list:
            # print('check node {}'.format(node.number))
            for i in range(len(link)):
                if node.number == link[i]:
                    nodes[i] = node
                    # print("find node {} in list".format(link[i]))
        for node in nodes:
            if node:
                self.node_list.remove(node)
        for i in range(len(nodes)):
            if not nodes[i]:
                nodes[i] = Node(link[i])
        nodes[0].links.append(nodes[1])
        nodes[1].links.append(nodes[0])
        for node in nodes:
            self.node_list.append(node)
        return


if __name__ == '__main__':
    a = [4, 3, 2, 1]
    a.reverse()
    a.remove(a[-1])
    b = [4, 5, 6, 7]
    print(a + b)
    solution = Solution()
    result = solution.restoreArray(
        [[100000, -100000]])
    print(result)
