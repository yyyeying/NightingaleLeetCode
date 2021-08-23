"""
给定一个按照升序排列的整数数组 nums，和一个目标值 target。找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回[-1, -1]。

进阶：

你可以设计并实现时间复杂度为O(log n)的算法解决此问题吗？

示例 1：

输入：nums = [5,7,7,8,8,10], target = 8
输出：[3,4]
示例2：

输入：nums = [5,7,7,8,8,10], target = 6
输出：[-1,-1]
示例 3：

输入：nums = [], target = 0
输出：[-1,-1]

提示：

0 <= nums.length <= 105
-109<= nums[i]<= 109
nums是一个非递减数组
-109<= target<= 109

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-first-and-last-position-of-element-in-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = 0
        mid = int(len(nums) / 2)
        right = len(nums) - 1
        while True:
            print('left: {}, right: {}, mid: {}'.format(left, right, mid))
            if left > right:
                return [-1, -1]
            if nums[mid] > target:
                right = mid - 1
                mid = left + int((right - left) / 2)
            elif nums[mid] < target:
                left = mid + 1
                mid = left + int((right - left) / 2)
            else:
                break
        print('mid: {}'.format(mid))
        result = [mid, mid]
        first = mid
        last = mid
        while first >= 0:
            print('first: {}'.format(first))
            if nums[first] == target:
                if first == 0:
                    result[0] = first
                first -= 1
            else:
                result[0] = first + 1
                break
        while last <= len(nums) - 1:
            print('last: {}'.format(last))
            if nums[last] == target:
                if last == len(nums) - 1:
                    result[1] = last
                last += 1
            else:
                result[1] = last - 1
                break
        return result


if __name__ == '__main__':
    solution = Solution()
    print(solution.searchRange([2, 2], 2))
