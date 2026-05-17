class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        magazine_map = {}

        for c in magazine:
            magazine_map[c] = magazine_map.get(c, 0) + 1

        for r in ransomNote:
            if r not in magazine_map or magazine_map[r] == 0:
                return False
            else:
                magazine_map[r] -= 1

        return True
