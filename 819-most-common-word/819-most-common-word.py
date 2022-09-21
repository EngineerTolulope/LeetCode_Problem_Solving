class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        paragraph = paragraph.lower()
        symbols = set(".!?',;")
        for symbol in symbols:
            paragraph = paragraph.replace(symbol, ' ')
    
        words = paragraph.split()
        word_count, banned = {}, set(banned)
        result, count = '', 0
        for word in words:
            if word in banned:
                continue
            word_count[word] = 1 + word_count.get(word, 0)
            
            if word_count[word] > count:
                result = word
                count = word_count[word]
        return result