class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        hash_map = {}
        res = 0

        for i in range(0, len(s)):
            if s[i] not in hash_map:
                hash_map[s[i]] = i

            else:
                res = max(res, i - hash_map[s[i]] - 1)

        return -1 if len(hash_map) == len(s) else res
