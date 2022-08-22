"""
给你一个字符串 s，找到 s 中最长的回文子串。

 

示例 1：

输入：s = "babad"
输出："bab"
解释："aba" 同样是符合题意的答案。
示例 2：

输入：s = "cbbd"
输出："bb"
 

提示：

1 <= s.length <= 1000
s 仅由数字和英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-palindromic-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) <= 0:
            return ""
        dp: List[List[bool]] = [[False] * len(s) for _ in range(len(s))]
        start = 0
        max_len = 1
        for i in range(len(s)):
            dp[i][i] = True
        for i in range(1, len(s)):
            for j in range(len(s) - i):
                if i == 1:
                    dp[j][j + i] = s[j] == s[j + i]
                else:
                    dp[j][j + i] = dp[j + 1][j + i - 1] and s[j] == s[j + i]
                # print("dp[{}][{}] = {}".format(j, j + i, dp[j][j + i]))
                if dp[j][j + i] is True:
                    start = j
                    max_len = i + 1
        return s[start: start + max_len]


if __name__ == '__main__':
    result = Solution().longestPalindrome("babad")
    print(result)
    result = Solution().longestPalindrome("cbbd")
    print(result)
