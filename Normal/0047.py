"""
给定一个可包含重复数字的序列 nums ，按任意顺序 返回所有不重复的全排列。

 

示例 1：

输入：nums = [1,1,2]
输出：
[[1,1,2],
 [1,2,1],
 [2,1,1]]
示例 2：

输入：nums = [1,2,3]
输出：[[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
 

提示：

1 <= nums.length <= 8
-10 <= nums[i] <= 10

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/permutations-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums = sorted(nums)

        def find(path: List[int], visited: List[bool]):
            # print("path = {}, {}, nums = {}".format(path, [nums[i] for i in path], nums))
            if len(path) == len(nums):
                result.append([nums[i] for i in path])
            for i in range(len(nums)):
                if i not in path:
                    if i > 0 and visited[i] is False and visited[i - 1] is False and nums[i] == nums[i - 1]:
                        continue
                    new_visited = list(visited)
                    new_visited[i] = True
                    path.append(i)
                    # print("append nums[{}] = {}, path = {}, {}".format(i, nums[i], path, [nums[i] for i in path]))
                    find(path, new_visited)
                    path.pop()

        find([], [False for _ in range(len(nums))])
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.permuteUnique([1, 1, 2])
    print(result)
    result = s.permuteUnique([1, 2, 3])
    print(result)
    result = s.permuteUnique([0, 1])
    print(result)
    result = s.permuteUnique([1])
    print(result)
    result = s.permuteUnique([1, 1])
    print(result)
    result = s.permuteUnique([])
    print(result)
