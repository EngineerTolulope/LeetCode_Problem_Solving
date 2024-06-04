class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_count = Counter("balloon")
        text_count = Counter(text)

        result = sys.maxsize
        for char, count in balloon_count.items():
            ratio = text_count[char] // count
            result = min(ratio, result)
        return result
