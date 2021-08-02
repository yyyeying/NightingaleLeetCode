"""
给定一个仅包含数字2-9的字符串，返回所有它能表示的字母组合。答案可以按 任意顺序 返回。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。


示例 1：

输入：digits = "23"
输出：["ad","ae","af","bd","be","bf","cd","ce","cf"]
示例 2：

输入：digits = ""
输出：[]
示例 3：

输入：digits = "2"
输出：["a","b","c"]

提示：

0 <= digits.length <= 4
digits[i] 是范围 ['2', '9'] 的一个数字。


来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        number_dict = {'2': ['a', 'b', 'c'],
                       '3': ['d', 'e', 'f'],
                       '4': ['g', 'h', 'i'],
                       '5': ['j', 'k', 'l'],
                       '6': ['m', 'n', 'o'],
                       '7': ['p', 'q', 'r', 's'],
                       '8': ['t', 'u', 'v'],
                       '9': ['w', 'x', 'y', 'z']}
        if len(digits) == 0:
            return []
        result = ['']
        for s in list(digits):
            str_queue = list(result)
            result = []
            while str_queue:
                temp_str = str_queue.pop()
                for i in number_dict[s]:
                    t = temp_str+i
                    result.append(t)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.letterCombinations('')
    print(result)
