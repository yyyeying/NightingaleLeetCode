"""
给出集合 [1,2,3,...,n]，其所有元素共有 n! 种排列。

按大小顺序列出所有排列情况，并一一标记，当 n = 3 时, 所有排列如下：

"123"
"132"
"213"
"231"
"312"
"321"
给定 n 和 k，返回第 k 个排列。

 

示例 1：

输入：n = 3, k = 3
输出："213"
示例 2：

输入：n = 4, k = 9
输出："2314"
示例 3：

输入：n = 3, k = 1
输出："123"
 

提示：

1 <= n <= 9
1 <= k <= n!

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/permutation-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        num = [i + 1 for i in range(n)]
        for i in range(k - 1):
            j = n - 2
            while num[j] >= num[j + 1]:
                j -= 1
            # print("j = {}".format(j))
            target = j + 1
            for m in range(j, n):
                if num[j] < num[m] <= num[target]:
                    target = m
            # print("target = {}".format(target))
            num[target], num[j] = num[j], num[target]
            # print(num)
            high = n - 1
            low = j + 1
            while low < high:
                num[high], num[low] = num[low], num[high]
                high -= 1
                low += 1
            # print("num = {}".format(num))
        return "".join([str(x) for x in num])


if __name__ == '__main__':
    s = Solution()
    result = s.getPermutation(3, 3)
    print(result)
    result = s.getPermutation(4, 9)
    print(result)
    result = s.getPermutation(3, 1)
    print(result)
