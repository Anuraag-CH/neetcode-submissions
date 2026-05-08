class Solution:
    def findLucky(self, arr: List[int]) -> int:

        max_value = -1
        hash_map = {}

        for i in arr:
            hash_map[i] = hash_map.get(i, 0) + 1

        for k, v in hash_map.items():
            if k == v:
                max_value = max(max_value, k)

        return max_value
