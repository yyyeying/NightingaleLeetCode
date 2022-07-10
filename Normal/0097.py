"""
给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。

两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串：

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ...
注意：a + b 意味着字符串 a 和 b 连接。

 

示例 1：


输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
输出：true
示例 2：

输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
输出：false
示例 3：

输入：s1 = "", s2 = "", s3 = ""
输出：true

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/interleaving-string
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        dp = [[False for _ in range(len(s2) + 1)] for _ in range(len(s1) + 1)]
        dp[0][0] = True
        # print(dp)
        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):
                # print("i = {}, j = {}".format(i, j))
                p = i + j - 1
                if i > 0:
                    # print("s1[{}] = {}, s3[{}] = {}".format(i - 1, s1[i - 1], p, s3[p]))
                    dp[i][j] = dp[i][j] or (dp[i - 1][j] and s1[i - 1] == s3[p])
                if j > 0:
                    # print("s2[{}] = {}, s3[{}] = {}".format(j - 1, s2[j - 1], p, s3[p]))
                    dp[i][j] = dp[i][j] or (dp[i][j - 1] and s2[j - 1] == s3[p])
        return dp[-1][-1]


if __name__ == '__main__':
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac"))
    print(Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc"))
    print(Solution().isInterleave(s1="a", s2="b", s3=""))
    print(Solution().isInterleave(s1="a", s2="", s3="a"))
