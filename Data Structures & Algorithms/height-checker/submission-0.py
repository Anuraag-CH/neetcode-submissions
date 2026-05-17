class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        new_heights = sorted(heights)

        res = 0

        for i in range(0, len(heights)):
            res += 1 if heights[i] != new_heights[i] else 0

        return res
