class Solution:
    def reverse(self, x: int) -> int:
        result = 0
        if x < 0:
            flag = False
            x = -x
        else:
            flag = True
        while x:
            result = 10 * result + x % 10
            x = int(x / 10)
        if result > 2**31-1 or result < -2**31:
            return 0
        else:
            return result if flag else -result