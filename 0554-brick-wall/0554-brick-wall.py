class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gaps = defaultdict(int)
        max_gaps = 0

        for row in wall:
            total = 0
            for brick in row[:-1]:
                total += brick
                count_gaps[total] += 1
                max_gaps = max(max_gaps, count_gaps[total])

        return len(wall) - max_gaps