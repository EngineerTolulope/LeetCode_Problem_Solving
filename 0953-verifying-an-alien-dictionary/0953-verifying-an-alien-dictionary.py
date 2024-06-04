class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        alpha_order = { char : index for index, char in enumerate(order)}

        for i in range(len(words) - 1):
            word_1, word_2 = words[i], words[i + 1]

            for j in range(len(word_1)):
                if j == len(word_2):
                    return False
                
                if word_1[j] != word_2[j]:
                    if alpha_order[word_2[j]] < alpha_order[word_1[j]]:
                        return False
                    break
        return True