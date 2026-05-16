class Solution:
    def validWordSquare(self, words: List[str]) -> bool:

        new_words = []

        rows = len(words)
        columns = len(words[0])

        for i in range(0, columns):
            new_word = ""
            for j in range(0, rows):
                if i < len(words[j]):
                    new_word += words[j][i]
            new_words.append(new_word)

        return words == new_words
