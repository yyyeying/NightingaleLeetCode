"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0) 。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/container-with-most-water
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        动态规划
        """
        max_area = 0
        left = 0
        right = len(height)-1
        while left < right:
            area = min(height[left], height[right])*(right-left)
            # print("left: {}, right: {}, area: {}".format(left, right, area))
            max_area = area if area > max_area else max_area
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_area

if __name__ == "__main__":
    solution = Solution()
    result = solution.maxArea([1,8,6,2,5,4,8,3,7])
    print(result)