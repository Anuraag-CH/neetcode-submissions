class Solution:
    def canPermutePalindrome(self, s: str) -> bool:

        hash_set = set()

        for i in s:
            if i in hash_set:
                hash_set.remove(i)
            else:
                hash_set.add(i)

        return True if len(hash_set) in [0, 1] else False
