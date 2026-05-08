class Solution:
    def areSentencesSimilar(
        self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]
    ) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        hash_set = set()

        for pair in similarPairs:
            hash_set.add((pair[0], pair[1]))
            hash_set.add((pair[1], pair[0]))

        for i in range(0, len(sentence1)):
            if sentence1[i] == sentence2[i]:
                continue
            if (sentence1[i], sentence2[i]) not in hash_set:
                return False

        return True
