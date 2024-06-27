class Solution:
    def minDeletions(self, s: str) -> int:
        char_count = Counter(s)

        result, visited = 0, set()
        for char, count in char_count.items():
            while count > 0 and count in visited:
                count -= 1
                result += 1
            visited.add(count)
        return result