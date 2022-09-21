class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []
        
        word_count = {}
        word_length = len(words[0])
        result = []
        words_length = len(words) * word_length
        
        for word in words:
            word_count[word] = 1 + word_count.get(word, 0)
            
        for left in range(len(s) - word_length + 1):
            words_seen = {}
            for right in range(len(words)):
                word_index = left + right * word_length
                temp_word = s[word_index:word_index + word_length]
                
                if temp_word not in word_count:
                    break
                    
                words_seen[temp_word] = words_seen.get(temp_word, 0) + 1
                if words_seen[temp_word] > word_count[temp_word]:
                    break
            if words_seen == word_count:
                result.append(left)
        return result