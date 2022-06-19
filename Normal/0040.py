"""
给定一个候选人编号的集合 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用 一次 。

注意：解集不能包含重复的组合。 

 

示例 1:

输入: candidates = [10,1,2,7,6,1,5], target = 8,
输出:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
示例 2:

输入: candidates = [2,5,2,1,2], target = 5,
输出:
[
[1,2,2],
[5]
]
 

提示:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/combination-sum-ii
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.target = target
        self.candidates = sorted(candidates)

        def backtrack(path: List[int]):
            real_path = [self.candidates[i] for i in path]
            sum_ = sum(real_path)
            # print("path: {}, sum: {}".format(real_path, sum_))
            if sum_ == self.target and sorted(real_path) not in self.result:
                self.result.append(sorted(real_path))
            elif sum_ < self.target:
                for i in range(path[-1] + 1, len(self.candidates)):
                    if i > path[-1] + 1 and self.candidates[i] == self.candidates[i - 1]:
                        continue
                    path.append(i)
                    backtrack(path)
                    path.pop()

        for i in range(len(self.candidates)):
            backtrack([i])
        return self.result


if __name__ == '__main__':
    s = Solution()
    result = s.combinationSum2([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], 27)
    # result = s.combinationSum2([10, 1, 2, 7, 6, 1, 5], 8)
    print(result)
