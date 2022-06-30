"""
给定一个 m x n 二维字符网格 board 和一个字符串单词 word 。如果 word 存在于网格中，返回 true ；否则，返回 false 。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

示例 1：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
输出：true
示例 2：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
输出：true
示例 3：


输入：board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
输出：false
 

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/word-search
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = [[False for _ in range(len(board[i]))] for i in range(len(board))]

        def dfs(path: List[List[int]]) -> bool:
            if len(path) == len(word):
                return True
            """print("path = {}, {}, finding {}, visited = {}"
                  .format(path, [board[i][j] for i, j in path], word[len(path)], visited))"""
            result: bool = False
            if path[-1][0] > 0:
                """print("path = {}, {}, finding {}, board[{}][{}] = {}, visited = {}"
                      .format(path, [board[i][j] for i, j in path], word[len(path)],
                              path[-1][0] - 1, path[-1][1],
                              board[path[-1][0] - 1][path[-1][1]],
                              visited[path[-1][0] - 1][path[-1][1]]))"""
                if word[len(path)] == board[path[-1][0] - 1][path[-1][1]] \
                        and visited[path[-1][0] - 1][path[-1][1]] is False:
                    visited[path[-1][0] - 1][path[-1][1]] = True
                    path.append([path[-1][0] - 1, path[-1][1]])
                    result = result or dfs(path)
                    path.pop()
                    visited[path[-1][0] - 1][path[-1][1]] = False
            if path[-1][0] < len(board) - 1:
                """print("path = {}, {}, finding {}, board[{}][{}] = {}, visited = {}"
                      .format(path, [board[i][j] for i, j in path], word[len(path)],
                              path[-1][0] + 1, path[-1][1],
                              board[path[-1][0] + 1][path[-1][1]],
                              visited[path[-1][0] + 1][path[-1][1]]))"""
                if word[len(path)] == board[path[-1][0] + 1][path[-1][1]] \
                        and visited[path[-1][0] + 1][path[-1][1]] is False:
                    visited[path[-1][0] + 1][path[-1][1]] = True
                    path.append([path[-1][0] + 1, path[-1][1]])
                    result = result or dfs(path)
                    path.pop()
                    visited[path[-1][0] + 1][path[-1][1]] = False
            if path[-1][1] > 0:
                """print("path = {}, {}, finding {}, board[{}][{}] = {}, visited = {}"
                      .format(path, [board[i][j] for i, j in path], word[len(path)],
                              path[-1][0], path[-1][1] - 1,
                              board[path[-1][0]][path[-1][1] - 1],
                              visited[path[-1][0]][path[-1][1] - 1]))"""
                if word[len(path)] == board[path[-1][0]][path[-1][1] - 1] \
                        and visited[path[-1][0]][path[-1][1] - 1] is False:
                    visited[path[-1][0]][path[-1][1] - 1] = True
                    path.append([path[-1][0], path[-1][1] - 1])
                    result = result or dfs(path)
                    path.pop()
                    visited[path[-1][0]][path[-1][1] - 1] = False
            if path[-1][1] < len(board[0]) - 1:
                """print("path = {}, {}, finding {}, board[{}][{}] = {}, visited = {}"
                      .format(path, [board[i][j] for i, j in path], word[len(path)],
                              path[-1][0], path[-1][1] + 1,
                              board[path[-1][0]][path[-1][1] + 1],
                              visited[path[-1][0]][path[-1][1] + 1]))"""
                if word[len(path)] == board[path[-1][0]][path[-1][1] + 1] \
                        and visited[path[-1][0]][path[-1][1] + 1] is False:
                    visited[path[-1][0]][path[-1][1] + 1] = True
                    path.append([path[-1][0], path[-1][1] + 1])
                    result = result or dfs(path)
                    path.pop()
                    visited[path[-1][0]][path[-1][1] + 1] = False
            return result

        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == word[0]:
                    visited[i][j] = True
                    if dfs([[i, j]]) is True:
                        return True
                    visited[i][j] = False
        return False


if __name__ == '__main__':
    s = Solution()
    result = s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCCED")
    print(result)
    result = s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="SEE")
    print(result)
    result = s.exist(board=[["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], word="ABCB")
    print(result)
