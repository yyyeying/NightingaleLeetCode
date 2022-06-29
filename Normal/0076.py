"""
给你一个字符串 s 、一个字符串 t 。返回 s 中涵盖 t 所有字符的最小子串。如果 s 中不存在涵盖 t 所有字符的子串，则返回空字符串 "" 。

 

注意：

对于 t 中重复字符，我们寻找的子字符串中该字符数量必须不少于 t 中该字符数量。
如果 s 中存在这样的子串，我们保证它是唯一的答案。
 

示例 1：

输入：s = "ADOBECODEBANC", t = "ABC"
输出："BANC"
示例 2：

输入：s = "a", t = "a"
输出："a"
示例 3:

输入: s = "a", t = "aa"
输出: ""
解释: t 中两个字符 'a' 均应包含在 s 的子串中，
因此没有符合条件的子字符串，返回空字符串。
 

提示：

1 <= s.length, t.length <= 105
s 和 t 由英文字母组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/minimum-window-substring
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import Dict, List


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        left: int = -1
        right: int = -1
        best = [0, len(s) - 1, len(s)]
        self.target: Dict[str, int] = {}
        self.window_count: Dict[str, int] = {}
        for c in t:
            if c not in self.target.keys():
                self.target.update({c: 1})
            else:
                self.target[c] += 1
        for k in self.target.keys():
            self.window_count.update({k: 0})
        for i in range(len(s)):
            if s[i] in self.target.keys():
                if left < 0:
                    left = i
                right = i
                self.window_count[s[i]] += 1
            while self.check() is True:
                if right - left + 1 < best[2]:
                    best = [left, right, right - left + 1]
                if s[left] in self.target.keys():
                    self.window_count[s[left]] -= 1
                left += 1
                if self.check() is False:
                    left -= 1
                    self.window_count[s[left]] += 1
                    break
        print(self.target, self.window_count)
        if self.check() is True:
            return s[best[0]: best[1] + 1]
        else:
            return ""

    def check(self) -> bool:
        for char, count in self.target.items():
            if self.window_count[char] < count:
                return False
        return True


if __name__ == '__main__':
    s = Solution()
    result = s.minWindow(s="ADOBECODEBANC", t="ABC")
    print(result)
    result = s.minWindow(s="A", t="A")
    print(result)
    result = s.minWindow(s="A", t="AA")
    print(result)
    result = s.minWindow("cabwefgewcwaefgcf", "cae")
    print(result)
