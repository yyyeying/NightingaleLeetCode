"""
罗马数字包含以下七种字符：I，V，X，L，C，D和M。

字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
例如， 罗马数字 2 写做II，即为两个并列的 1。12 写做XII，即为X+II。 27 写做XXVII, 即为XX+V+II。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做IIII，而是IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为IX。这个特殊的规则只适用于以下六种情况：

I可以放在V(5) 和X(10) 的左边，来表示 4 和 9。
X可以放在L(50) 和C(100) 的左边，来表示 40 和90。
C可以放在D(500) 和M(1000) 的左边，来表示400 和900。
给你一个整数，将其转为罗马数字。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/integer-to-roman
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""


class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = [['M', 1000],
                      ['D', 500],
                      ['C', 100],
                      ['L', 50],
                      ['X', 10],
                      ['V', 5],
                      ['I', 1]]
        roman_list = []
        for item in roman_dict:
            a = int(num / item[1])
            roman_list.append(a)
            num -= a * item[1]
        # print(roman_list)
        roman_num = ''
        for i in range(0, len(roman_list), 2):
            # print('{}, {}'.format(i-1, i))
            # print('{}, {}'.format(roman_list[i-1], roman_list[i]))
            if roman_list[i] == 4:
                # print('{} = 4'.format(roman_list[i]))
                if roman_list[i-1] == 0:
                    roman_num += roman_dict[i][0]
                    roman_num += roman_dict[i-1][0]
                elif roman_list[i-1] == 1:
                    roman_num += roman_dict[i][0]
                    roman_num += roman_dict[i-2][0]
            else:
                for j in [i-1, i]:
                    if j >= 0:
                        for k in range(roman_list[j]):
                            roman_num += roman_dict[j][0]
        return roman_num


if __name__ == '__main__':
    solution = Solution()
    result = solution.intToRoman(1994)
    print(result)