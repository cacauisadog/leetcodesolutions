# https://leetcode.com/problems/longest-common-prefix/


class Solution:
    def findCommonPrefix(self, str1: str, str2: str) -> str:
        common_prefix = ""
        i = 0

        try:
            while str1[i] == str2[i]:
                common_prefix += str1[i]
                i += 1
        except IndexError:
            pass

        return common_prefix

    def longestCommonPrefix(self, strs: list[str]) -> str:
        if len(strs) == 1:
            return strs[0]

        common_prefix = self.findCommonPrefix(strs[0], strs[1])
        if len(strs) == 2:
            return common_prefix

        for str in strs[2:]:
            common_prefix = self.findCommonPrefix(common_prefix, str)

        return common_prefix
