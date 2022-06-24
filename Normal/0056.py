"""
以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。
请你合并所有重叠的区间，并返回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。

 

示例 1：

输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
输出：[[1,6],[8,10],[15,18]]
解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
示例 2：

输入：intervals = [[1,4],[4,5]]
输出：[[1,5]]
解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。
 

提示：

1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/merge-intervals
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key=lambda x: x[0])
        i = 0
        while i < len(intervals) - 1:
            # print(i, intervals)
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i + 1][1], intervals[i][1])
                del intervals[i + 1]
            else:
                i += 1
        return intervals


if __name__ == '__main__':
    s = Solution()
    result = s.merge([[1, 3], [2, 6], [8, 10], [15, 18]])
    print(result)
    result = s.merge([[1, 4], [4, 5]])
    print(result)
    result = s.merge([[1, 4], [2, 3]])
    print(result)
