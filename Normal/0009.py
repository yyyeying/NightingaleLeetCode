class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_list = list(str(x))
        x_reverse = list(x_list)
        x_reverse.reverse()
        print(x_reverse)
        result = x_list == x_reverse
        return result

if __name__ == '__main__':
    solution = Solution()
    result = solution.isPalindrome(-121)
    print(result)