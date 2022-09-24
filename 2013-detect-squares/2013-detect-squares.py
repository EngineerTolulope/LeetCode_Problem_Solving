class DetectSquares:

    def __init__(self):
        self.point_count = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.point_count[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        result = 0
        x2, y2 = point
        for x1, y1 in list(self.point_count):
            if abs(y2 - y1) != abs(x2 - x1) or x1 == x2 or y1 == y2:
                continue
            result += (self.point_count[(x1, y1)] * 
                       self.point_count[(x2, y1)] *
                       self.point_count[(x1, y2)])
        return result


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)