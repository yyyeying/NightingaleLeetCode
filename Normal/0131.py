"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。

回文串 是正着读和反着读都一样的字符串。

 

示例 1：

输入：s = "aab"
输出：[["a","a","b"],["aa","b"]]
示例 2：

输入：s = "a"
输出：[["a"]]
 

提示：

1 <= s.length <= 16
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-partitioning
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def partition(self, s: str) -> List[List[str]]:
        is_palindrome = [[True for _ in range(len(s))] for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i + 1, len(s)):
                # print(i, j)
                is_palindrome[i][j] = is_palindrome[i + 1][j - 1] and s[i] == s[j]
        stack = []
        result = []
        for i in range(len(s)):
            if is_palindrome[0][i] is True:
                stack.append([[0, i]])
        # stack = [[[0, i]] for i in range(len(s))]
        while len(stack) > 0:
            path = stack.pop()
            # print(path)
            last = path[-1][1]
            if last == len(s) - 1:
                result.append(list(path))
                continue
            for i in range(last + 1, len(s)):
                # print("i={}".format(i))
                if is_palindrome[last + 1][i] is True:
                    stack.append(list(path) + [[last + 1, i]])
        real_result = []
        for path in result:
            strs = []
            for x, y in path:
                # print(x, y)
                strs.append(s[x:y + 1])
            real_result.append(strs)
        return real_result


if __name__ == '__main__':
    result = Solution().partition("aab")
    print(result)
    result = Solution().partition("a")
    print(result)
