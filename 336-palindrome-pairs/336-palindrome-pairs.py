class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        def get_prefixes(word):
            result = []
            for i in range(len(word)):
                if word[i:] == word[i:][::-1]:
                    result.append(word[:i])
            return result
        
        def get_suffixes(word):
            result = []
            for i in range(len(word)):
                if word[:i+1] == word[:i+1][::-1]:
                    result.append(word[i+1:])
            return result
        
        
        word_index = {word:i for i, word in enumerate(words)}
        result = []
        
        for i, word in enumerate(words):
            reversed_word = word[::-1]
            if reversed_word in word_index:
                if i != word_index[reversed_word]:
                    result.append([i, word_index[reversed_word]])
            
            for word_prefix in get_prefixes(word):
                reversed_prefix = word_prefix[::-1]
                if reversed_prefix in word_index:
                    result.append([i, word_index[reversed_prefix]])
                
            for word_suffix in get_suffixes(word):
                reversed_suffix = word_suffix[::-1]
                if reversed_suffix in word_index:
                    result.append([word_index[reversed_suffix], i])
        return result
                    
            
        
        
        