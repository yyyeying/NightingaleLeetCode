"""
有 n 个网络节点，标记为1到 n。

给你一个列表times，表示信号经过 有向 边的传递时间。times[i] = (ui, vi, wi)，其中ui是源节点，vi是目标节点， wi是一个信号从源节点传递到目标节点的时间。

现在，从某个节点K发出一个信号。需要多久才能使所有节点都收到信号？如果不能使所有节点收到信号，返回-1 。


示例 1：



输入：times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
输出：2
示例 2：

输入：times = [[1,2,1]], n = 2, k = 1
输出：1
示例 3：

输入：times = [[1,2,1]], n = 2, k = 2
输出：-1

提示：

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
所有 (ui, vi) 对都 互不相同（即，不含重复边）

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/network-delay-time
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        result = 0
        verticies = self.construct_graph(times, n)
        # print(verticies)
        visited = {i: 101 for i in list(range(1, n+1))}
        visited[k] = 0
        # print(visited)
        node_queue = [k]
        while node_queue:
            node = node_queue.pop()
            # print(node)
            for v in verticies[node]:
                if v[1] + visited[node] < visited[v[0]]:
                    visited[v[0]] = v[1] + visited[node]
                    node_queue.insert(0, v[0])
        result = max(visited.values())
        if result > 100:
            return -1
        return result

    def construct_graph(self, raw_verticies: List[List[int]], n: int):
        vertices = {i: [] for i in range(1, n+1)}
        # print(raw_verticies)
        for v in raw_verticies:
            if v[0] in vertices.keys():
                vertices[v[0]].append([v[1], v[2]])
        return vertices


if __name__ == '__main__':
    solution = Solution()
    result = solution.networkDelayTime([[1,2,1]], 2,2)
    print(result)
