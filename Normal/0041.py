"""
给你一个未排序的整数数组 nums ，请你找出其中没有出现的最小的正整数。

请你实现时间复杂度为 O(n) 并且只使用常数级别额外空间的解决方案。
 

示例 1：

输入：nums = [1,2,0]
输出：3
示例 2：

输入：nums = [3,4,-1,1]
输出：2
示例 3：

输入：nums = [7,8,9,11,12]
输出：1
 

提示：

1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/first-missing-positive
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i] - 1]:
                # print("nums[{}] = {}, swap nums[{}] and nums[{}]".format(i, nums[i], nums[i] - 1, i))
                temp = nums[i] - 1
                nums[i], nums[temp] = nums[temp], nums[i]
                # print(nums)
        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1
        return len(nums) + 1


if __name__ == '__main__':
    s = Solution()
    result = s.firstMissingPositive([1, 1])
    print(result)
