"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"
 

提示：

每个字符串仅由字符 '0' 或 '1' 组成。
1 <= a.length, b.length <= 10^4
字符串如果不是 "0" ，就都不含前导零。

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/add-binary
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        plus = 0
        i = len(a) - 1
        j = len(b) - 1
        result = []
        while i >= 0 or j >= 0:
            # print("a[{}] = {}, b[{}] = {}, plus = {}".format(i, a[i], j, b[j], plus))
            temp = plus
            if i >= 0:
                temp += int(a[i])
                i -= 1
            if j >= 0:
                temp += int(b[j])
                j -= 1
            if temp >= 2:
                plus = 1
                result.insert(0, str(temp - 2))
            else:
                plus = 0
                result.insert(0, str(temp))
        if plus == 1:
            result.insert(0, str(plus))
        return "".join(result)


if __name__ == '__main__':
    s = Solution()
    result = s.addBinary("11", "1")
    print(result)
    result = s.addBinary("1", "1")
    print(result)
    result = s.addBinary("1010", "1011")
    print(result)
