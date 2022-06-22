"""
给你一个 m 行 n 列的矩阵 matrix ，请按照 顺时针螺旋顺序 ，返回矩阵中的所有元素。

 

示例 1：


输入：matrix = [[1,2,3],[4,5,6],[7,8,9]]
输出：[1,2,3,6,9,8,7,4,5]
示例 2：


输入：matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
输出：[1,2,3,4,8,12,11,10,9,5,6,7]
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/spiral-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        direction = 0
        visited = [[False for _ in range(len(matrix[0]))] for _ in range(len(matrix))]
        pos = [0, 0]
        next_pos = [0, 0]
        result = []
        while True:
            print(pos)
            result.append(matrix[pos[0]][pos[1]])
            visited[pos[0]][pos[1]] = True
            flag = False
            change_dir = 0
            while flag is False and change_dir <= 3:
                dir = direction % 4
                if dir == 0:
                    next_pos = [pos[0], pos[1] + 1]
                elif dir == 1:
                    next_pos = [pos[0] + 1, pos[1]]
                elif dir == 2:
                    next_pos = [pos[0], pos[1] - 1]
                elif dir == 3:
                    next_pos = [pos[0] - 1, pos[1]]
                print("next_pos: {}".format(next_pos))
                if next_pos[0] >= len(matrix) \
                        or next_pos[1] >= len(matrix[0]) or visited[next_pos[0]][next_pos[1]] is True:
                    direction += 1
                    change_dir += 1
                else:
                    pos = next_pos
                    flag = True
            if change_dir == 4:
                break
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.spiralOrder([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(result)
    result = s.spiralOrder([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])
    print(result)

