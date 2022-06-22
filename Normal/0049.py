"""给你一个字符串数组，请你将 字母异位词 组合在一起。可以按任意顺序返回结果列表。

字母异位词 是由重新排列源单词的字母得到的一个新单词，所有源单词中的字母通常恰好只用一次。

 

示例 1:

输入: strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
输出: [["bat"],["nat","tan"],["ate","eat","tea"]]
示例 2:

输入: strs = [""]
输出: [[""]]
示例 3:

输入: strs = ["a"]
输出: [["a"]]
 

提示：

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] 仅包含小写字母

来源：力扣（LeetCode）
链接：https://leetcode.cn/problems/group-anagrams
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。"""
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = ["".join(sorted(s)) for s in strs]
        print(sorted_strs)
        result_dict = {}
        for i in range(len(strs)):
            if sorted_strs[i] not in result_dict.keys():
                result_dict.update({sorted_strs[i]: [strs[i]]})
            else:
                result_dict[sorted_strs[i]].append(strs[i])
        result = list(result_dict.values())
        return result


if __name__ == '__main__':
    s = Solution()
    result = s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
    print(result)
