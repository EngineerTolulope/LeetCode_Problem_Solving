class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        chars_count = Counter(chars)
        result = 0

        for word in words:
            word_count = defaultdict(int)
            still_good = True
            for char in word:
                word_count[char] += 1
            
                if char not in chars_count or word_count[char] > chars_count[char]:
                    still_good = False
                    break
            
            if still_good:
                result += len(word)
        return result
                
                
