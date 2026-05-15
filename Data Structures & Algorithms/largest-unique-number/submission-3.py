class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        hash_map = {}

        for n in nums:
            hash_map[n] = hash_map.get(n, 0) + 1

        max_num = -1

        for i in hash_map:
            if hash_map[i] == 1:
                max_num = max(max_num, i)

        return max_num
