"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""
from typing import Dict, List


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        character = {}
        result = 0
        begin = 0
        for i in range(len(s)):
            if s[i] in character.keys():
                begin = max(character[s[i]] + 1, begin)
            result = max(result, i - begin + 1)
            character[s[i]] = i
        return result


class Solution2:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        character: Dict[str, int] = {s[0]: 0}
        dp: List[int] = [0 for _ in range(len(s))]
        dp[0] = 1
        for i in range(1, len(s)):
            if s[i] not in character.keys():
                dp[i] = dp[i - 1] + 1
            else:
                dp[i] = min(dp[i - 1] + 1, i - character[s[i]])
            character[s[i]] = i
        # print(dp)
        return max(dp)


if __name__ == '__main__':
    print(Solution2().lengthOfLongestSubstring("abcabcbb"))
    print(Solution2().lengthOfLongestSubstring("bbbbb"))
    print(Solution2().lengthOfLongestSubstring("pwwkew"))
    print(Solution2().lengthOfLongestSubstring("p"))
