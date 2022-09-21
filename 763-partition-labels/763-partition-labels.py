class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_index = {} # char -> last index
        for i, char in enumerate(s):
            last_index[char] = i
        
        size, end, result = 0, 0, []
        for i, char in enumerate(s):
            size += 1
            end = max(end, last_index[char])
            if end == i:
                result.append(size)
                size = 0
        return result