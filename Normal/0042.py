"""
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。

 

示例 1：



输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
输出：6
解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。
示例 2：

输入：height = [4,2,0,3,2,5]
输出：9
 

提示：

n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/trapping-rain-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        left = [0 for _ in range(len(height))]
        right = [0 for _ in range(len(height))]
        for i in range(1, len(height)):
            left[i] = max(height[i - 1], left[i - 1])
        for i in reversed(range(len(height) - 1)):
            right[i] = max(height[i + 1], right[i + 1])
        rain = 0
        for i in range(len(height)):
            rain += (min(left[i], right[i]) - height[i]) if min(left[i], right[i]) > height[i] else 0
        return rain


if __name__ == '__main__':
    s = Solution()
    result = s.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1])
    print(result)
    result = s.trap([4, 2, 0, 3, 2, 5])
    print(result)
