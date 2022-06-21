"""
给出一个字符串数组 words 组成的一本英语词典。返回 words 中最长的一个单词，该单词是由 words 词典中其他单词逐步添加一个字母组成。

若其中有多个可行的答案，则返回答案中字典序最小的单词。若无答案，则返回空字符串。



示例 1：

输入：words = ["w","wo","wor","worl", "world"]
输出："world"
解释： 单词"world"可由"w", "wo", "wor", 和 "worl"逐步添加一个字母组成。
示例 2：

输入：words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
输出："apple"
解释："apply" 和 "apple" 都能由词典中的单词组成。但是 "apple" 的字典序小于 "apply"


提示：

1 <= words.length <= 1000
1 <= words[i].length <= 30
所有输入的字符串 words[i] 都只包含小写字母。

https://leetcode-cn.com/problems/longest-word-in-dictionary/
"""

from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        length = [len(w) for w in words]
        max_length = 0
        results = []
        while max(length) >= 0:
            candidate = words[length.index(max(length))]
            # print("candidate: {}".format(candidate))
            candidate_flag = [False for i in range(len(candidate))]
            for x in words:
                if x in candidate[:len(x)]:
                    # print("x: {} find".format(x))
                    candidate_flag[len(x) - 1] = True
            # print(candidate_flag)
            if candidate_flag == [True for i in range(len(candidate))] and len(candidate) >= max_length:
                max_length = len(candidate)
                results.append(candidate)
            length[length.index(max(length))] = -1
        results = sorted(results)
        # print(results)
        if len(results) > 0:
            return results[0]
        else:
            return ""


if __name__ == '__main__':
    w = ["wo","wor","worl","world"]
    solution = Solution()
    result = solution.longestWord(words=w)
    print(result)
