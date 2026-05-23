class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:

        pattern = [p for p in pattern]
        s = [i for i in s.split(" ")]

        if len(pattern) != len(s):
            return False

        pattern_map_s = {}
        s_map_pattern = {}

        for i in range(0, len(pattern)):
            if pattern[i] in pattern_map_s and pattern_map_s[pattern[i]] != s[i]:
                return False
            if s[i] in s_map_pattern and s_map_pattern[s[i]] != pattern[i]:
                return False

            pattern_map_s[pattern[i]] = s[i]
            s_map_pattern[s[i]] = pattern[i]

        return True
