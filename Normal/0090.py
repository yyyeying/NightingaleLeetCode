"""
给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。

 

示例 1：

输入：nums = [1,2,2]
输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/subsets-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        def dfs(path: List[int]):
            # print(path)
            result.append([nums[i] for i in path])
            if len(path) == len(nums):
                return
            start = path[-1] + 1 if len(path) > 0 else 0
            for i in range(start, len(nums)):
                if i != start and nums[i] == nums[i - 1]:
                    continue
                path.append(i)
                dfs(path)
                path.pop()

        dfs([])
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.subsetsWithDup([1, 2, 2])
    print(result)
