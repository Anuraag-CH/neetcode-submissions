class Solution:
    def countElements(self, arr: List[int]) -> int:

        set_arr = set(arr)
        count = 0
        for i in arr:
            if i + 1 in set_arr:
                count += 1
        return count
