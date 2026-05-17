class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:

        char_map = {}
        res = 0

        def word_in_char_set(word):
            new_char_map = char_map.copy()
            for w in word:
                if w not in new_char_map or new_char_map[w] == 0:
                    return 0
                else:
                    new_char_map[w] -= 1
            return len(word)

        for c in chars:
            char_map[c] = char_map.get(c, 0) + 1

        for word in words:
            res += word_in_char_set(word)

        return res
