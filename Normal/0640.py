"""
求解一个给定的方程，将x以字符串 "x=#value" 的形式返回。该方程仅包含 '+' ， '-' 操作，变量 x 和其对应系数。

如果方程没有解，请返回 "No solution" 。如果方程有无限解，则返回 “Infinite solutions” 。

如果方程中只有一个解，要保证返回值 'x' 是一个整数。

 

示例 1：

输入: equation = "x+5-3+x=6+x-2"
输出: "x=2"
示例 2:

输入: equation = "x=x"
输出: "Infinite solutions"
示例 3:

输入: equation = "2x=x"
输出: "x=0"
 

 

提示:

3 <= equation.length <= 1000
equation 只有一个 '='.
equation 方程由整数组成，其绝对值在 [0, 100] 范围内，不含前导零和变量 'x' 。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/solve-the-equation
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def solveEquation(self, equation: str) -> str:
        x_value = 0
        const_value = 0
        left = True
        add = True
        value = 0
        for i in range(len(equation)):
            if equation[i] == "=":
                if add is True:
                    const_value += value
                else:
                    const_value -= value
                left = False
                add = False
                value = 0
            elif equation[i] == "+":
                if add is True:
                    const_value += value
                else:
                    const_value -= value
                if left is True:
                    add = True
                else:
                    add = False
                value = 0
            elif equation[i] == "-":
                if add is True:
                    const_value += value
                else:
                    const_value -= value
                if left is True:
                    add = False
                else:
                    add = True
                value = 0
            elif equation[i] == "x":
                if add is True:
                    if value > 0:
                        x_value += value
                    else:
                        if i - 1 >= 0 and equation[i - 1] == "0":
                            pass
                        else:
                            x_value += 1
                else:
                    if value > 0:
                        x_value -= value
                    else:
                        if i - 1 >= 0 and equation[i - 1] == "0":
                            pass
                        else:
                            x_value -= 1
                value = 0
            else:
                value = value * 10 + int(equation[i])
        if value > 0:
            if add is True:
                const_value += value
            else:
                const_value -= value
        if x_value == 0:
            if const_value == 0:
                result = "Infinite solutions"
            else:
                result = "No solution"
        else:
            result = "x=" + str(int(-const_value / x_value))
        return result


if __name__ == '__main__':
    result = Solution().solveEquation("x+5-3+x=6+x-2")
    print(result)
    result = Solution().solveEquation("x=x")
    print(result)
    result = Solution().solveEquation("2x=x")
    print(result)
    result = Solution().solveEquation("2=0")
    print(result)
    result = Solution().solveEquation("0x=0")
    print(result)
    result = Solution().solveEquation("x=100")
    print(result)
    result = Solution().solveEquation("0=0x")
    print(result)
