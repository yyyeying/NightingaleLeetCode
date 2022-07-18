"""
给你一个字符串 s 和一个字符串列表 wordDict 作为字典。请你判断是否可以利用字典中出现的单词拼接出 s 。

注意：不要求字典中出现的单词全部都使用，并且字典中的单词可以重复使用。

 

示例 1：

输入: s = "leetcode", wordDict = ["leet", "code"]
输出: true
解释: 返回 true 因为 "leetcode" 可以由 "leet" 和 "code" 拼接成。
示例 2：

输入: s = "applepenapple", wordDict = ["apple", "pen"]
输出: true
解释: 返回 true 因为 "applepenapple" 可以由 "apple" "pen" "apple" 拼接成。
     注意，你可以重复使用字典中的单词。
示例 3：

输入: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
输出: false
 

提示：

1 <= s.length <= 300
1 <= wordDict.length <= 1000
1 <= wordDict[i].length <= 20
s 和 wordDict[i] 仅有小写英文字母组成
wordDict 中的所有字符串 互不相同

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/word-break
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            print("i = {}".format(i))
            for w in wordDict:
                print("word = {}, s = {}, i+len = {}".format(w, s[i:i + len(w)], i + len(w)))
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i] or dp[i + len(w)] if i + len(w) < len(s) else True
        # print(dp)
        return dp[0]


if __name__ == '__main__':
    result = Solution().wordBreak(s="applepenapple", wordDict=["apple", "pen"])
    print(result)
    result = Solution().wordBreak(s="catsandog", wordDict=["cats", "dog", "sand", "and", "cat"])
    print(result)
    result = Solution().wordBreak("cars", ["car", "ca", "rs"])
    print(result)
    """result = Solution().wordBreak(
        s="aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
          "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaab",
        wordDict=["a", "aa", "aaa", "aaaa", "aaaaa", "aaaaaa", "aaaaaaa", "aaaaaaaa", "aaaaaaaaa", "aaaaaaaaaa"])
    print(result)"""