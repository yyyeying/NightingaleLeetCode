"""
给定一个不含重复数字的数组 nums ，返回其 所有可能的全排列 。你可以 按任意顺序 返回答案。

 

示例 1：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
示例 2：

输入：nums = [0,1]
输出：[[0,1],[1,0]]
示例 3：

输入：nums = [1]
输出：[[1]]

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/permutations
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result = []

        def find(path: List[int]):
            # print(path)
            if len(path) == len(nums):
                result.append([nums[i] for i in path])
            for i in range(len(nums)):
                if i not in path:
                    path.append(i)
                    find(path)
                    path.pop()

        for i in range(len(nums)):
            find([i])
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.permute([1, 2, 3])
    print(result)
    result = s.permute([0, 1])
    print(result)
    result = s.permute([1])
    print(result)
    result = s.permute([])
    print(result)
