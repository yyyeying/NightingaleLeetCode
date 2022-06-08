import functools
from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        def sort_rules(x, y):
            if x + y > y + x:
                return 1
            elif x + y < y + x:
                return -1
            else:
                return 0

        strnum = [str(num) for num in nums]
        strnum.sort(key=functools.cmp_to_key(sort_rules))
        return "".join(strnum)


if __name__ == '__main__':
    s = Solution()
    print(s.minNumber([3, 30, 34, 5, 9]))
