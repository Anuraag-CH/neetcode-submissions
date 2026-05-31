class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:

        hash_set = set()

        if len(nums) == 1 :
            return False

        for i in range(0, k + 1):
            if i < len(nums):
                hash_set.add(nums[i])
            else:
                break

        if len(hash_set) < k + 1:
            return True

        for i in range(k + 1, len(nums)):
            hash_set.remove(nums[i - k - 1])

            if nums[i] in hash_set:
                return True

            hash_set.add(nums[i])

        return False
