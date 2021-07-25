"""
请你来实现一个myAtoi(string s)函数，使其能将字符串转换成一个 32 位有符号整数（类似 C/C++ 中的 atoi 函数）。

函数myAtoi(string s) 的算法如下：

读入字符串并丢弃无用的前导空格
检查下一个字符（假设还未到字符末尾）为正还是负号，读取该字符（如果有）。 确定最终结果是负数还是正数。 如果两者都不存在，则假定结果为正。
读入下一个字符，直到到达下一个非数字字符或到达输入的结尾。字符串的其余部分将被忽略。
将前面步骤读入的这些数字转换为整数（即，"123" -> 123， "0032" -> 32）。如果没有读入数字，则整数为 0 。必要时更改符号（从步骤 2 开始）。
如果整数数超过 32 位有符号整数范围 [−2^31, 2^31− 1] ，需要截断这个整数，使其保持在这个范围内。具体来说，小于 −2^31 的整数应该被固定为 −2^31 ，大于 2^31− 1 的整数应该被固定为 2^31− 1 。
返回整数作为最终结果。
注意：

本题中的空白字符只包括空格字符 ' ' 。
除前导空格或数字后的其余字符串外，请勿忽略 任何其他字符。
"""


class Solution:
    def myAtoi(self, s: str) -> int:
        number = 0
        negative = False
        first = True
        end = False
        for character in list(s):
            # print(ord(character))
            if character == '-' and first:
                negative = True
                first = False
            elif character == '+' and first:
                first = False
            elif ord(character) == 32 and first:
                pass
            elif 48 <= ord(character) <= 57 and not end:
                first = False
                number = 10*number+int(character)
            else:
                end = True
        if negative:
            number = -number
        if number <= -2**31:
            number = -2**31
        elif number >= 2**31-1:
            number = 2**31-1
        return number


if __name__ == '__main__':
    solution = Solution()
    number = solution.myAtoi(' +0 123')
    print(number)
