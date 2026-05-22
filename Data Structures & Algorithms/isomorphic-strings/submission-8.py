class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        s_map_t = {}
        t_map_s = {}

        for i in range(0, len(s)):
            if s[i] in s_map_t and s_map_t[s[i]] != t[i]:
                return False
            else:
                s_map_t[s[i]] = t[i]

        for i in range(0, len(t)):
            if t[i] in t_map_s and t_map_s[t[i]] != s[i]:
                return False
            else:
                t_map_s[t[i]] = s[i]

        return True
