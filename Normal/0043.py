"""
给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

注意：不能使用任何内置的 BigInteger 库或直接将输入转换为整数。

 

示例 1:

输入: num1 = "2", num2 = "3"
输出: "6"
示例 2:

输入: num1 = "123", num2 = "456"
输出: "56088"
 

提示：

1 <= num1.length, num2.length <= 200
num1 和 num2 只能由数字组成。
num1 和 num2 都不包含任何前导零，除了数字0本身。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/multiply-strings
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        for i in range(len(num1)):
            for j in range(len(num2)):
                result += (ord(num1[i]) - ord("0")) * (ord(num2[j]) - ord("0")) * 10 ** (
                            len(num1) - i + len(num2) - j - 2)
        return str(result)


if __name__ == '__main__':
    s = Solution()
    result = s.multiply("123", "456")
    print(result)
    result = s.multiply("0", "0")
    print(result)
    result = s.multiply("6913259244",
                        "71103343")
    print(result)
