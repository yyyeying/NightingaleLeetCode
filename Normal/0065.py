"""
有效数字（按顺序）可以分成以下几个部分：

一个 小数 或者 整数
（可选）一个 'e' 或 'E' ，后面跟着一个 整数
小数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
下述格式之一：
至少一位数字，后面跟着一个点 '.'
至少一位数字，后面跟着一个点 '.' ，后面再跟着至少一位数字
一个点 '.' ，后面跟着至少一位数字
整数（按顺序）可以分成以下几个部分：

（可选）一个符号字符（'+' 或 '-'）
至少一位数字
部分有效数字列举如下：["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"]

部分无效数字列举如下：["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"]

给你一个字符串 s ，如果 s 是一个 有效数字 ，请返回 true 。

 

示例 1：

输入：s = "0"
输出：true
示例 2：

输入：s = "e"
输出：false
示例 3：

输入：s = "."
输出：false
 

提示：

1 <= s.length <= 20
s 仅含英文字母（大写和小写），数字（0-9），加号 '+' ，减号 '-' ，或者点 '.' 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/valid-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isNumber(self, s: str) -> bool:
        numbers = [str(i) for i in range(10)]
        es = ["E", "e"]
        point = ["."]
        signs = ["+", "-"]
        e_flag = False
        point_flag = False
        sign_flag = False
        num_flag = False
        for i in range(len(s)):
            if i == 0 and s[i] not in signs and s[i] not in numbers and s[i] not in point:
                return False
            if s[i] in point:
                if point_flag is False and len(s) > 1:
                    point_flag = True
                else:
                    # print("Error in point")
                    return False
            elif s[i] in signs:
                # print("sign")
                if sign_flag is True:
                    # print("Error in sign")
                    return False
                elif (i == 0 and len(s) > 1) or s[i - 1] in es and i < len(s) - 1:
                    sign_flag = True
                else:
                    # print("Error in sign")
                    return False
            elif s[i] in es:
                if num_flag is False or e_flag is True or i == len(s) - 1 or i == 0 or (i == 1 and s[i - 1] in point):
                    # print("Error in E")
                    return False
                elif i > 0:
                    e_flag = True
                    point_flag = True
                    sign_flag = False
            elif s[i] in numbers:
                num_flag = True
            else:
                # print("Error in other")
                return False
        if num_flag is True:
            return True
        else:
            # print("Error in num")
            return False


if __name__ == '__main__':
    s = Solution()
    test_case = [".1", "2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93",
                 "-123.456e789", "3.", "+.8",
                 "abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53", ".", ".e1", "6+1", "4e+", "+.", "+E3", "46.E3"]
    for t in test_case:
        print(t, s.isNumber(t))
