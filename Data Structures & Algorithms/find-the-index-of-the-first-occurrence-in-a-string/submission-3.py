class Solution:
    def strStr(self, haystack: str, needle: str) -> int:

        if len(haystack) < len(needle):
            return -1

        for j in range(0, len(haystack) - len(needle) + 1):
            if haystack[j : j + len(needle)] == needle:
                return j

        return -1
