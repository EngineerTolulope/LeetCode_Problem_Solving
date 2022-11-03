class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        current_max = -1
        for i in range(len(arr) - 1, -1, -1):
            new_max = max(current_max, arr[i])
            arr[i] = current_max
            current_max = new_max
        return arr
            