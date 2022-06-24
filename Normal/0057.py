"""
给你一个 无重叠的 ，按照区间起始端点排序的区间列表。

在列表中插入一个新的区间，你需要确保列表中的区间仍然有序且不重叠（如果有必要的话，可以合并区间）。

 

示例 1：

输入：intervals = [[1,3],[6,9]], newInterval = [2,5]
输出：[[1,5],[6,9]]
示例 2：

输入：intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
输出：[[1,2],[3,10],[12,16]]
解释：这是因为新的区间 [4,8] 与 [3,5],[6,7],[8,10] 重叠。
示例 3：

输入：intervals = [], newInterval = [5,7]
输出：[[5,7]]
示例 4：

输入：intervals = [[1,5]], newInterval = [2,3]
输出：[[1,5]]
示例 5：

输入：intervals = [[1,5]], newInterval = [2,7]
输出：[[1,7]]
 

提示：

0 <= intervals.length <= 104
intervals[i].length == 2
0 <= intervals[i][0] <= intervals[i][1] <= 105
intervals 根据 intervals[i][0] 按 升序 排列
newInterval.length == 2
0 <= newInterval[0] <= newInterval[1] <= 105

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/insert-interval
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # print("intervals: {}, newIntervals = {}".format(intervals, newInterval))
        i = 0
        inserted = False
        if len(intervals) > 0 and newInterval[0] <= intervals[0][0]:
            intervals.insert(0, newInterval)
            inserted = True
        while inserted is False and i < len(intervals) - 1:
            if intervals[i][0] <= newInterval[0] <= intervals[i + 1][0]:
                intervals.insert(i + 1, newInterval)
                inserted = True
                break
            else:
                i += 1
        if inserted is False:
            intervals.append(newInterval)
        # print(i, intervals)
        # print(intervals[i][1], newInterval[1])
        while i < len(intervals) - 1:
            # print(i, intervals)
            if intervals[i][1] >= intervals[i + 1][0]:
                intervals[i][1] = max(intervals[i][1], intervals[i + 1][1])
                del intervals[i + 1]
            else:
                if intervals[i][1] > newInterval[1]:
                    break
                i += 1
        return intervals


if __name__ == '__main__':
    s = Solution()
    result = s.insert(intervals=[[1, 3], [6, 9]], newInterval=[2, 5])
    print(result)
    result = s.insert(intervals=[[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], newInterval=[4, 8])
    print(result)
    result = s.insert(intervals=[[1, 5]], newInterval=[2, 7])
    print(result)
    result = s.insert(intervals=[[1, 5]], newInterval=[2, 3])
    print(result)
    result = s.insert(intervals=[], newInterval=[5, 7])
    print(result)
    result = s.insert(intervals=[[1, 5]], newInterval=[0, 3])
    print(result)
