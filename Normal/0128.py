"""
给定一个未排序的整数数组 nums ，找出数字连续的最长序列（不要求序列元素在原数组中连续）的长度。

请你设计并实现时间复杂度为 O(n) 的算法解决此问题。

 

示例 1：

输入：nums = [100,4,200,1,3,2]
输出：4
解释：最长数字连续序列是 [1, 2, 3, 4]。它的长度为 4。
示例 2：

输入：nums = [0,3,7,2,5,8,4,6,0,1]
输出：9
 

提示：

0 <= nums.length <= 105
-109 <= nums[i] <= 109

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/longest-consecutive-sequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_dict = {}
        max_length = 0
        for n in nums:
            if n not in hash_dict.keys():
                left = hash_dict[n - 1] if n - 1 in hash_dict.keys() else 0
                right = hash_dict[n + 1] if n + 1 in hash_dict.keys() else 0
                # print(left, right)
                current_length = left + right + 1
                max_length = max(current_length, max_length)
                hash_dict[n] = current_length
                hash_dict[n - left] = current_length
                hash_dict[n + right] = current_length
                # print(hash_dict)
        return max_length


if __name__ == '__main__':
    result = Solution().longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1])
    print(result)
