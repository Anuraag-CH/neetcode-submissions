class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum = []
        cur_sum = 0
        for n in nums:
            cur_sum += n
            self.prefix_sum.append(cur_sum)

    def sumRange(self, left: int, right: int) -> int:

        return self.prefix_sum[right] - self.prefix_sum[left] + self.nums[left]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
