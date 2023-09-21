class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        count_gaps = {0 : 0}
        for row in wall:
            total = 0
            for brick in row[:-1]:
                total += brick
                count_gaps[total] = count_gaps.get(total, 0) + 1
        return len(wall) - max(count_gaps.values())