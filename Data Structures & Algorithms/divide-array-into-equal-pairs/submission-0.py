class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        hash_set = set()

        for n in nums:
            if n not in hash_set:
                hash_set.add(n)
            else:
                hash_set.remove(n)

        return True if len(hash_set) == 0 else False
