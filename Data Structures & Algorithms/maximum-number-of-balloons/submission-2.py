class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:

        hash_map = {}

        for t in text:
            if t in "balon":
                hash_map[t] = hash_map.get(t, 0) + 1

        hash_map["l"] = hash_map.get("l", 0) // 2
        hash_map["o"] = hash_map.get("o", 0) // 2

        return min(hash_map.values())
