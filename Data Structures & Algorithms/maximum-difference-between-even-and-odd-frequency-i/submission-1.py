class Solution:
    def maxDifference(self, s: str) -> int:

        dict_s = {}

        for i in s:
            dict_s[i] = dict_s.get(i, 0) + 1

        max_odd_frequency = float("-inf")
        max_even_frequency = float("-inf")
        min_odd_frequency = float("inf")
        min_even_frequency = float("inf")

        for i in dict_s.values():
            if i % 2 == 0:
                max_even_frequency = max(max_even_frequency, i)
                min_even_frequency = min(min_even_frequency, i)
            else:
                max_odd_frequency = max(max_odd_frequency, i)
                min_odd_frequency = min(min_odd_frequency, i)

        return max_odd_frequency - min_even_frequency
