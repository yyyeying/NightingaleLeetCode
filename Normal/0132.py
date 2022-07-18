"""
给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是回文。

返回符合要求的 最少分割次数 。

 

示例 1：

输入：s = "aab"
输出：1
解释：只需一次分割就可将 s 分割成 ["aa","b"] 这样两个回文子串。
示例 2：

输入：s = "a"
输出：0
示例 3：

输入：s = "ab"
输出：1
 

提示：

1 <= s.length <= 2000
s 仅由小写英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/palindrome-partitioning-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def minCut(self, s: str) -> int:
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
        real_result = [len(p) - 1 for p in result]
        return min(real_result)


if __name__ == '__main__':
    result = Solution().minCut("aab")
    print(result)
