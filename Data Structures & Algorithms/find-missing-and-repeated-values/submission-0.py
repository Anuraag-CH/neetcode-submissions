class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        n = len(grid) ** 2
        check_set = set([i for i in range(1, n + 1)])

        res = []
        for g in grid:
            for i in g:
                if i in check_set:
                    check_set.remove(i)
                else:
                    res.append(i)

        for i in check_set:
            res.append(i)
        return res
