class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:

        hash_set = set()
        for n in nums:
            hash_set.add(n)
        res = []
        for i in range(1, len(nums) + 1):
            if i not in hash_set:
                res.append(i)
        return res
