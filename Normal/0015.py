"""
给你一个包含 n 个整数的数组nums，判断nums中是否存在三个元素 a，b，c ，使得a + b + c = 0 ？请你找出所有和为 0 且不重复的三元组。

注意：答案中不可以包含重复的三元组。


示例 1：

输入：nums = [-1,0,1,2,-1,-4]
输出：[[-1,-1,2],[-1,0,1]]
示例 2：

输入：nums = []
输出：[]
示例 3：

输入：nums = [0]
输出：[]

提示：

0 <= nums.length <= 3000
-105 <= nums[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/3sum
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def threeSumOld(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        for i in nums:
            # print(i)
            new_nums = list(nums)
            new_nums.remove(i)
            new_nums = sorted(new_nums)
            # print(new_nums)
            left = 0
            right = len(new_nums) - 1
            while left < right:
                sum_ = new_nums[left] + new_nums[right] + i
                # print('left: {}, right: {}, sum: {}'.format(left, right, sum_))
                if sum_ > 0:
                    right -= 1
                elif sum_ < 0:
                    left += 1
                else:
                    new_result = sorted([new_nums[left], new_nums[right], i])
                    if new_result not in result:
                        result.append(new_result)
                    new_nums.remove(new_nums[left])
                    new_nums.remove(new_nums[right - 1])
                    left = 0
                    right = len(new_nums) - 1
        return result

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = []
        if len(nums) < 3:
            return result
        nums = sorted(nums)
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                new_nums = list(nums)
                target = - new_nums[i] - new_nums[j]
                left = 0
                right = len(new_nums) - 1
                index = int((right - left) / 2)
                print('left: {}, right: {}, index: {}'.format(left, right, index))
                while index != left and index != right:
                    print('left: {}, right: {}, index: {}'.format(left, right, index))
                    if new_nums[index] > target:
                        right = index - 1
                        index = int((right - left) / 2)
                    elif new_nums[index] < target:
                        left = index + 1
                        index = int((right - left) / 2)
                    else:
                        new_result = [new_nums[index], new_nums[i], new_nums[j]]
                        if new_result not in result:
                            result.append(new_result)
                        new_nums.remove(new_nums[i])
                        new_nums.remove(new_nums[j-1])
                        left = 0
                        right = len(new_nums) - 1
                        index = int((right - left) / 2)
        return result


if __name__ == '__main__':
    solution = Solution()
    result = solution.threeSum([-1,0,1,2,-1,-4])
    print(result)
