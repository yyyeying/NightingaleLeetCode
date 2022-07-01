"""
给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。

求在该柱状图中，能够勾勒出来的矩形的最大面积。

 

示例 1:



输入：heights = [2,1,5,6,2,3]
输出：10
解释：最大的矩形为图中红色区域，面积为 10
示例 2：



输入： heights = [2,4]
输出： 4
 

提示：

1 <= heights.length <=105
0 <= heights[i] <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/largest-rectangle-in-histogram
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        result = 0
        for i in range(len(heights)):
            left = i
            right = i
            while left >= 0 and heights[left] >= heights[i]:
                left -= 1
            while right < len(heights) and heights[right] >= heights[i]:
                right += 1
            new_area = heights[i] * (right - left - 1)
            result = max(result, new_area)
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.largestRectangleArea([2, 1, 5, 6, 2, 3])
    print(result)
    result = s.largestRectangleArea([2, 4])
    print(result)
    result = s.largestRectangleArea([1, 1, 1, 1, 1, 1, 1, 1])
    print(result)
    result = s.largestRectangleArea([4, 2, 0, 3, 2, 5])
    print(result)
