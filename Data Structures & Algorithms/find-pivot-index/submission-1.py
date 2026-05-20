class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        prefix_sum = []

        cur_sum = 0
        for n in range(0, len(nums)):
            prefix_sum.append(cur_sum)
            cur_sum += nums[n]

        suffix_sum = []

        cur_sum = 0

        for n in range(len(nums) - 1, -1, -1):
            suffix_sum.insert(0, cur_sum)
            cur_sum += nums[n]

        for i in range(0, len(nums)):
            if prefix_sum[i] == suffix_sum[i]:
                return i

        return -1
