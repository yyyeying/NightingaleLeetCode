"""
给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。

 

示例 1：


输入：n = 3
输出：[[1,2,3],[8,9,4],[7,6,5]]
示例 2：

输入：n = 1
输出：[[1]]
 

提示：

1 <= n <= 20

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/spiral-matrix-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        direction = 0
        result = [[0 for _ in range(n)] for _ in range(n)]
        row = 0
        col = 0
        step = 0
        step_count = 0
        step_end = n
        for i in range(n * n):
            """print("i+1: {}, row: {}, col: {}, step: {}, step_count: {}, step_end: {}, direction: {}".format(i + 1, row,
                                                                                                            col, step,
                                                                                                            step_count,
                                                                                                            step_end,
                                                                                                            direction))"""
            result[row][col] = i + 1
            step += 1
            if step == step_end:
                direction += 1
                step_count += 1
                step = 0
            if (step_end < n and step_count == 2) or (step_end == n and step_count == 1):
                step_end -= 1
                step_count = 0
            dir = direction % 4
            if dir == 0:
                col += 1
            elif dir == 1:
                row += 1
            elif dir == 2:
                col -= 1
            elif dir == 3:
                row -= 1
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.generateMatrix(1)
    print(result)
    result = s.generateMatrix(2)
    print(result)
    result = s.generateMatrix(3)
    print(result)
    result = s.generateMatrix(4)
    print(result)
    result = s.generateMatrix(5)
    print(result)
