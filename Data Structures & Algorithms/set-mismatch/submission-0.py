class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:

        check_arr = set([i for i in range(1, len(nums) + 1)])

        res = []
        for n in nums:
            if n in check_arr:
                check_arr.remove(n)
            else:
                res.append(n)

        for i in check_arr:
            res.append(i)

        return res
