class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:

        word1_list = []
        word2_list = []

        for i in range(0, len(wordsDict)):
            if wordsDict[i] == word1:
                word1_list.append(i)
            if wordsDict[i] == word2:
                word2_list.append(i)

        shortest_distance = len(wordsDict)

        for i in word1_list:
            for j in word2_list:
                shortest_distance = min(shortest_distance, abs(i - j))

        return shortest_distance
