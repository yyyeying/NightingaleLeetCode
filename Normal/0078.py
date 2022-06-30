"""
给你一个整数数组 nums ，数组中的元素 互不相同 。返回该数组所有可能的子集（幂集）。

解集 不能 包含重复的子集。你可以按 任意顺序 返回解集。

 

示例 1：

输入：nums = [1,2,3]
输出：[[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
示例 2：

输入：nums = [0]
输出：[[],[0]]
 

提示：

1 <= nums.length <= 10
-10 <= nums[i] <= 10
nums 中的所有元素 互不相同

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/subsets
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def dfs(path: List[int]):
            result.append([nums[i] for i in path])
            if len(path) > 0:
                i = path[-1] + 1
            else:
                i = 0
            while i < len(nums):
                path.append(i)
                dfs(path)
                i += 1
                path.pop()

        dfs([])
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.subsets([1, 2, 3])
    print(result)
    result = s.subsets([1])
    print(result)
