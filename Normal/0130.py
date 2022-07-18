"""
给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充。
 

示例 1：


输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
示例 2：

输入：board = [["X"]]
输出：[["X"]]
 

提示：

m == board.length
n == board[i].length
1 <= m, n <= 200
board[i][j] 为 'X' 或 'O'

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/surrounded-regions
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = [[False for _ in range(len(board[i]))] for i in range(len(board))]
        modify_list = []
        for i in range(len(board)):
            for j in range(len(board[i])):
                # visited[i][j] = True
                if board[i][j] == "O" and visited[i][j] is False:
                    stack: List[List[int]] = [[i, j]]
                    area = []
                    modify_flag = True
                    while len(stack) > 0:
                        cur_x, cur_y = stack.pop()
                        visited[cur_x][cur_y] = True
                        area.append([cur_x, cur_y])
                        if cur_x == 0 or cur_x == len(board) - 1 or cur_y == 0 or cur_y == len(board[cur_x]) - 1:
                            modify_flag = False
                        for x, y in [[cur_x - 1, cur_y], [cur_x, cur_y - 1], [cur_x + 1, cur_y], [cur_x, cur_y + 1]]:
                            if 0 <= x < len(board) and 0 <= y < len(board[x]) \
                                    and board[x][y] == "O" \
                                    and visited[x][y] is False:
                                stack.append([x, y])
                    # print(area)
                    if modify_flag is True:
                        modify_list += area
        for x, y in modify_list:
            board[x][y] = "X"


if __name__ == '__main__':
    board = [["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]]
    Solution().solve(board)
    print(board)
