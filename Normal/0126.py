"""
按字典 wordList 完成从单词 beginWord 到单词 endWord 转化，一个表示此过程的 转换序列 是形式上像 beginWord -> s1 -> s2 -> ... -> sk 这样的单词序列，并满足：

每对相邻的单词之间仅有单个字母不同。
转换过程中的每个单词 si（1 <= i <= k）必须是字典 wordList 中的单词。注意，beginWord 不必是字典 wordList 中的单词。
sk == endWord
给你两个单词 beginWord 和 endWord ，以及一个字典 wordList 。请你找出并返回所有从 beginWord 到 endWord 的 最短转换序列 ，如果不存在这样的转换序列，返回一个空列表。每个序列都应该以单词列表 [beginWord, s1, s2, ..., sk] 的形式返回。

 

示例 1：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
输出：[["hit","hot","dot","dog","cog"],["hit","hot","lot","log","cog"]]
解释：存在 2 种最短的转换序列：
"hit" -> "hot" -> "dot" -> "dog" -> "cog"
"hit" -> "hot" -> "lot" -> "log" -> "cog"
示例 2：

输入：beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
输出：[]
解释：endWord "cog" 不在字典 wordList 中，所以不存在符合要求的转换序列。
 

提示：

1 <= beginWord.length <= 5
endWord.length == beginWord.length
1 <= wordList.length <= 500
wordList[i].length == beginWord.length
beginWord、endWord 和 wordList[i] 由小写英文字母组成
beginWord != endWord
wordList 中的所有单词 互不相同

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/word-ladder-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List, Dict


class Path:
    def __init__(self, wordList: List[str]):
        self.link: Dict[str, List[str]] = {}
        self.word_list = wordList
        self.construct()
        # print(self.link)

    def construct(self):
        for word in self.word_list:
            self.link.update({word: []})
            for drow in self.word_list:
                if self.distance(word, drow) == 1:
                    self.link[word].append(drow)

    def distance(self, a: str, b: str):
        ptr = 0
        distance = 0
        while ptr < len(a):
            if a[ptr] != b[ptr]:
                distance += 1
            ptr += 1
            if distance >= 2:
                break
        return distance


class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        p = Path(wordList + [beginWord])
        result: List[List[str]] = []

        queue: List[List[str]] = [[beginWord]]
        min_length = 501

        while len(queue) > 0:
            path = queue.pop()
            # print(path)
            if path[-1] == endWord and len(path) <= min_length:
                result.append(path)
                min_length = min(min_length, len(path))
            if len(path) > min_length:
                continue
            for word in p.link[path[-1]]:
                if word not in path:
                    new_path = path + [word]
                    queue.insert(0, new_path)
        return result


if __name__ == '__main__':
    result = Solution().findLadders(beginWord="hit", endWord="cog", wordList=["hot", "dot", "dog", "lot", "log", "cog"])
    print(result)
    result = Solution().findLadders("qa",
                                    "sq",
                                    ["si", "go", "se", "cm", "so", "ph", "mt", "db", "mb", "sb", "kr", "ln", "tm", "le",
                                     "av", "sm", "ar", "ci", "ca", "br", "ti", "ba", "to", "ra", "fa", "yo", "ow", "sn",
                                     "ya", "cr", "po", "fe", "ho", "ma", "re", "or", "rn", "au", "ur", "rh", "sr", "tc",
                                     "lt", "lo", "as", "fr", "nb", "yb", "if", "pb", "ge", "th", "pm", "rb", "sh", "co",
                                     "ga", "li", "ha", "hz", "no", "bi", "di", "hi", "qa", "pi", "os", "uh", "wm", "an",
                                     "me", "mo", "na", "la", "st", "er", "sc", "ne", "mn", "mi", "am", "ex", "pt", "io",
                                     "be", "fm", "ta", "tb", "ni", "mr", "pa", "he", "lr", "sq", "ye"])
    print(result)
