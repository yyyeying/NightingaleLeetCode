"""
给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串 的长度。
"""


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
