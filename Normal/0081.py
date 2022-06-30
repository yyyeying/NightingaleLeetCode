"""
已知存在一个按非降序排列的整数数组 nums ，数组中的值不必互不相同。

在传递给函数之前，nums 在预先未知的某个下标 k（0 <= k < nums.length）上进行了 旋转 ，
使数组变为 [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
（下标 从 0 开始 计数）。例如， [0,1,2,4,4,4,5,6,6,7] 在下标 5 处经旋转后可能变为 [4,5,6,6,7,0,1,2,4,4] 。

给你 旋转后 的数组 nums 和一个整数 target ，请你编写一个函数来判断给定的目标值是否存在于数组中。
如果 nums 中存在这个目标值 target ，则返回 true ，否则返回 false 。

你必须尽可能减少整个操作步骤。

 

示例 1：

输入：nums = [2,5,6,0,0,1,2], target = 0
输出：true
示例 2：

输入：nums = [2,5,6,0,0,1,2], target = 3
输出：false
 

提示：

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
题目数据保证 nums 在预先未知的某个下标上进行了旋转
-104 <= target <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-in-rotated-sorted-array-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if len(nums) == 0:
            return False
        elif len(nums) == 1:
            return nums[0] == target
        start = len(nums) - 2
        while nums[start] <= nums[start + 1]:
            start -= 1
            if start < 0:
                break
        start += 1
        # print(start)

        def binary_search(low, high) -> bool:
            if low > high:
                return False
            mid = low + int((high - low) / 2)
            real_mid = (start + mid) % len(nums)
            """print("low = {}, high = {}, mid = {}, nums[mid] = {}".format((low + start) % len(nums),
                                                                         (high + start) % len(nums), 
                                                                         real_mid, nums[real_mid]))"""
            if nums[real_mid] == target:
                return True
            elif nums[real_mid] > target:
                return binary_search(low, mid - 1)
            elif nums[real_mid] < target:
                return binary_search(mid + 1, high)

        return binary_search(0, len(nums) - 1)


if __name__ == '__main__':
    s = Solution()
    result = s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=0)
    print(result)
    result = s.search(nums=[2, 5, 6, 0, 0, 1, 2], target=3)
    print(result)
    result = s.search(nums=[0, 1, 2, 3, 4, 5], target=0)
    print(result)
    result = s.search(nums=[1], target=0)
    print(result)
    result = s.search(nums=[1, 1], target=0)
    print(result)
