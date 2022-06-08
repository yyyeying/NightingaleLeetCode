"""
从若干副扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这5张牌是不是连续的。2～10为数字本身，A为1，J为11，Q为12，K为13，而大、小王为 0 ，可以看成任意数字。A 不能视为 14。

 

示例 1:

输入: [1,2,3,4,5]
输出: True
 

示例 2:

输入: [0,0,1,2,5]
输出: True
 

限制：

数组长度为 5 

数组的数取值为 [0, 13] .

通过次数160,848提交次数349,069

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/bu-ke-pai-zhong-de-shun-zi-lcof
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def isStraight(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        count = 0
        current = 0
        start = False
        i = 0
        while i < len(nums):
            print(nums[i])
            if nums[i] == 0:
                count += 1
                i += 1
            elif start is False:
                start = True
                current = nums[i]
                i += 1
            else:
                if nums[i] == current + 1:
                    current += 1
                    i += 1
                elif count > 0:
                    count -= 1
                    current += 1
                else:
                    return False
        return True


if __name__ == '__main__':
    s = Solution()
    print(s.isStraight([1, 2, 12, 0, 3]))
