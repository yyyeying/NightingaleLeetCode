"""
有效 IP 地址 正好由四个整数（每个整数位于 0 到 255 之间组成，且不能含有前导 0），整数之间用 '.' 分隔。

例如："0.1.2.201" 和 "192.168.1.1" 是 有效 IP 地址，但是 "0.011.255.245"、"192.168.1.312" 和 "192.168@1.1" 是 无效 IP 地址。
给定一个只包含数字的字符串 s ，用以表示一个 IP 地址，返回所有可能的有效 IP 地址，这些地址可以通过在 s 中插入 '.' 来形成。你 不能 重新排序或删除 s 中的任何数字。你可以按 任何 顺序返回答案。

 

示例 1：

输入：s = "25525511135"
输出：["255.255.11.135","255.255.111.35"]
示例 2：

输入：s = "0000"
输出：["0.0.0.0"]
示例 3：

输入：s = "101023"
输出：["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
 

提示：

1 <= s.length <= 20
s 仅由数字组成

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/restore-ip-addresses
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(path: List[int], i: int):
            # print("path: {}".format(path))
            if i == len(s) and len(path) == 4:
                result.append("{}.{}.{}.{}".format(path[0], path[1], path[2], path[3]))
                return
            elif i == len(s) or len(path) == 4:
                return
            j = i + 1
            while int(s[i:j]) < 256 and j <= len(s):
                # print("candidate: {}".format(s[i:j]))
                if j == i + 1 or (j > i + 1 and s[i] != "0"):
                    path.append(int(s[i:j]))
                    backtrack(path, j)
                    path.pop()
                j += 1

        backtrack([], 0)
        return result


if __name__ == '__main__':
    result = Solution().restoreIpAddresses("101023")
    print(result)
    result = Solution().restoreIpAddresses("0000")
    print(result)
    result = Solution().restoreIpAddresses("25525511135")
    print(result)
