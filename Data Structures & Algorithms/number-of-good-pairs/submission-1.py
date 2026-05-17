class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        res = 0

        hash_map = {}

        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1

        for h in hash_map:
            res += (hash_map[h] * (hash_map[h] - 1)) // 2
        
        return res
