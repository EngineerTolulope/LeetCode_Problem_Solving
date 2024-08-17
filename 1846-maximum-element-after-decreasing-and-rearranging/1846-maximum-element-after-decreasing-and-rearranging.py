class Solution:
    def maximumElementAfterDecrementingAndRearranging(self, arr: List[int]) -> int:
        arr.sort()

        previous = 0
        for num in arr:
            previous = min(previous + 1, num)
        return previous