class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:

        hash_set = {}

        for a in arr:
            hash_set[a] = hash_set.get(a, 0) + 1

        for a in arr:
            if hash_set[a] == 1:
                k -= 1

                if k == 0:
                    return a

        return ""
