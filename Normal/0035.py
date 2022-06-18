"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

请必须使用时间复杂度为 O(log n) 的算法。

 

示例 1:

输入: nums = [1,3,5,6], target = 5
输出: 2
示例 2:

输入: nums = [1,3,5,6], target = 2
输出: 1
示例 3:

输入: nums = [1,3,5,6], target = 7
输出: 4
 

提示:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums 为 无重复元素 的 升序 排列数组
-104 <= target <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-insert-position
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        self.nums = nums
        return self.binary_search(0, len(nums) - 1, target)

    def binary_search(self, low, high, target) -> int:
        print("low: {}, high:{}".format(low, high))
        if low > high:
            if low >= len(self.nums):
                return low
            elif self.nums[low] > target:
                return low
            else:
                return low - 1
        mid = int(low + (high - low) / 2)
        if self.nums[mid] == target:
            return mid
        elif self.nums[mid] > target:
            return self.binary_search(low, mid - 1, target)
        else:
            return self.binary_search(mid + 1, high, target)


if __name__ == '__main__':
    s = Solution()
    print(s.searchInsert([1, 3, 5, 7, 9, 11], 10))
