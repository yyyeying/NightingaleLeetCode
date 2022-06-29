"""
给定两个整数 n 和 k，返回范围 [1, n] 中所有可能的 k 个数的组合。

你可以按 任何顺序 返回答案。

 

示例 1：

输入：n = 4, k = 2
输出：
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
示例 2：

输入：n = 1, k = 1
输出：[[1]]
 

提示：

1 <= n <= 20
1 <= k <= n

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combinations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        self.result = []
        self.n = n
        self.k = k
        self.dfs([])
        return self.result

    def dfs(self, path):
        # print("path: {}, n = {}, k = {}".format(path, self.n, self.k))
        if len(path) == self.k:
            # print("get path {}".format(path))
            self.result.append(list(path))
            return
        for i in range(1, self.n + 1):
            if len(path) == 0 or i > path[-1]:
                path.append(i)
                self.dfs(path)
                path.pop()


if __name__ == '__main__':
    s = Solution()
    result = s.combine(4, 3)
    print(result)
    result = s.combine(4, 2)
    print(result)
    result = s.combine(1, 1)
    print(result)
