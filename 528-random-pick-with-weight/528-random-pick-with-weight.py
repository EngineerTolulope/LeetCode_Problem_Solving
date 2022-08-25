class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = []
        current_sum = 0
        for weight in w:
            current_sum += weight
            self.prefix_sum.append(current_sum)
        self.total_sum = current_sum
        

    def pickIndex(self) -> int:
        random_num = self.total_sum * random.random()
        left, right = 0, len(self.prefix_sum)
        while left < right:
            middle = left + (right - left) // 2
            if self.prefix_sum[middle] <= random_num:
                left = middle + 1
            else:
                right = middle
        return left


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()