"""
编写一个高效的算法来判断 m x n 矩阵中，是否存在一个目标值。该矩阵具有如下特性：

每行中的整数从左到右按升序排列。
每行的第一个整数大于前一行的最后一个整数。
 

示例 1：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
输出：true
示例 2：


输入：matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
输出：false
 

提示：

m == matrix.length
n == matrix[i].length
1 <= m, n <= 100
-104 <= matrix[i][j], target <= 104

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/search-a-2d-matrix
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List, Union


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag, row = self.binarySearch([m[0] for m in matrix], target, 0, len(matrix))
        if flag is True:
            return True
        elif row >= 0:
            real_flag, col = self.binarySearch(matrix[row], target, 0, len(matrix[row]))
            return real_flag
        else:
            return False

    def binarySearch(self, array: List[int], target: int, start: int, end: int) -> List[Union[bool, int]]:
        print("array: {}, start: {}, end: {}".format(array, start, end))
        if start > end:
            return [False, -1]
        mid = start + int((end - start) / 2)
        if array[mid] == target:
            return [True, mid]
        elif array[mid] > target:
            return self.binarySearch(array, target, start, mid - 1)
        elif array[mid] < target:
            if mid == len(array) - 1 or array[mid + 1] > target:
                return [False, mid]
            else:
                return self.binarySearch(array, target, mid + 1, end)


if __name__ == '__main__':
    s = Solution()
    result = s.searchMatrix(matrix=[[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=3)
    print(result)
    result = s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], target=13)
    print(result)
    result = s.searchMatrix([[1]], 2)
    print(result)
