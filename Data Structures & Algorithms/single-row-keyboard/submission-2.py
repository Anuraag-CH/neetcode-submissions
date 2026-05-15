class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:

        hash_map = {}
        res = 0

        for k in range(0, len(keyboard)):
            hash_map[keyboard[k]] = k

        prev_index = 0

        for w in range(0, len(word)):
            cur_index = hash_map[word[w]]

            res += abs(cur_index - prev_index)

            prev_index = cur_index

        return res
