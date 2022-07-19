"""
给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续子数组（该子数组中至少包含一个数字），并返回该子数组所对应的乘积。

测试用例的答案是一个 32-位 整数。

子数组 是数组的连续子序列。

 

示例 1:

输入: nums = [2,3,-2,4]
输出: 6
解释: 子数组 [2,3] 有最大乘积 6。
示例 2:

输入: nums = [-2,0,-1]
输出: 0
解释: 结果不能为 2, 因为 [-2,-1] 不是子数组。
 

提示:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
nums 的任何前缀或后缀的乘积都 保证 是一个 32-位 整数

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/maximum-product-subarray
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_ = [nums[0] for _ in range(len(nums))]
        min_ = [nums[0] for _ in range(len(nums))]
        for i in range(1, len(nums)):
            max_[i] = max(min_[i - 1] * nums[i], max_[i - 1] * nums[i], nums[i])
            min_[i] = min(max_[i - 1] * nums[i], min_[i - 1] * nums[i], nums[i])
        return max(max(max_), max(min_))


if __name__ == '__main__':
    result = Solution().maxProduct([-2, 0, -1])
    print(result)
    result = Solution().maxProduct([-3, -1, -1])
    print(result)
