class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        min_len = len(strs[0])
        for _str in strs:
            min_len = min(min_len, len(_str))

        res = ""

        for i in range(0, min_len):
            for _str in strs:
                if strs[0][i] != _str[i]:
                    return res
            res += strs[0][i]

        return res
