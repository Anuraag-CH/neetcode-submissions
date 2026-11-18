class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:

        if len(nums) == 1:
            return True

        # smallest

        small = nums[0]

        # largest
        large = nums[0]

        for n in nums:
            if n < small:
                small = n
            if n > large:
                large = n

        # check small to large range
        length = len(nums)
        nums = set(nums)

        for n in range(small, small + length):
            if n not in nums:
                return False

        return True
