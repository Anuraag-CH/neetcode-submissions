class Solution:
    def maxScore(self, s: str) -> int:
        max_res = 0
        ones_list = []

        ones = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "1":
                ones += 1
            ones_list.insert(0, ones)

        zeroes = 0

        for i in range(0, len(s) - 1):
            if s[i] == "0":
                zeroes += 1
            res = zeroes + ones_list[i + 1]
            max_res = max(res, max_res)

        return max_res
