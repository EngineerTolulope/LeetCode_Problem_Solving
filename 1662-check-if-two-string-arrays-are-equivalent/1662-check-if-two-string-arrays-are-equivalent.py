class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        w1, w2 = 0, 0  # Indices for word1 and word2
        i, j = 0, 0    # Indices within the current strings
        
        while w1 < len(word1) and w2 < len(word2):
            # Compare characters at the current positions
            if word1[w1][i] != word2[w2][j]:
                return False
            
            # Move to the next character in both strings
            i += 1
            j += 1
            
            # If we reach the end of the current string in word1
            if i == len(word1[w1]):
                w1 += 1
                i = 0
            
            # If we reach the end of the current string in word2
            if j == len(word2[w2]):
                w2 += 1
                j = 0
        
        # Ensure both lists are fully traversed
        return w1 == len(word1) and w2 == len(word2)
