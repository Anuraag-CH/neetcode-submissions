class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:

        longest_increasing = 1
        longest_decreasing = 1

        current_increasing = 1
        current_decreasing = 1

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                current_increasing += 1
                current_decreasing = 1
                longest_increasing = max(longest_increasing, current_increasing)
            elif nums[i] < nums[i - 1]:
                current_increasing = 1
                current_decreasing += 1
                longest_decreasing = max(longest_decreasing, current_decreasing)

            else:
                current_increasing = 1
                current_decreasing = 1

        print(longest_increasing, longest_decreasing)
        return max(longest_increasing, longest_decreasing)
