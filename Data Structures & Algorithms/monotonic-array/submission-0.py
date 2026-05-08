class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        def is_increasing(nums):

            for i in range(1, len(nums)):
                if nums[i] < nums[i - 1]:
                    return False

            return True

        def is_decreasing(nums):

            for i in range(1, len(nums)):
                if nums[i] > nums[i - 1]:
                    return False

            return True

        return is_increasing(nums) or is_decreasing(nums)
