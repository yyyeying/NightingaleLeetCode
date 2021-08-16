"""
给定一个只包括 '('，')'，'{'，'}'，'['，']'的字符串 s ，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。

示例 1：

输入：s = "()"
输出：true

示例2：

输入：s = "()[]{}"
输出：true

示例3：

输入：s = "(]"
输出：false

示例4：

输入：s = "([)]"
输出：false

示例5：

输入：s = "{[]}"
输出：true

提示：

1 <= s.length <= 104
s 仅由括号 '()[]{}' 组成

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-parentheses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isValid(self, s: str) -> bool:
        s_list = list(s)
        right_list = [')', ']', '}']
        left_list = ['(', '[', '{']
        stack = []
        if len(s_list) == 1:
            return False
        while len(s_list) > 0:
            character = s_list.pop()
            if character in right_list:
                stack.append(character)
            elif character in left_list:
                if len(stack) == 0:
                    return False
                candidate = stack.pop()
                if right_list.index(candidate) != left_list.index(character):
                    return False
        if len(stack) == 0:
            return True
        else:
            return False


if __name__ == '__main__':
    s = ')(){}'
    solution = Solution()
    print(solution.isValid(s))
