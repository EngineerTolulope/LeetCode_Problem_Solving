class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        left, right = 0, len(arr) - k
        
        while left < right:
            middle = (left +  right) // 2
            if x - arr[middle] > arr[middle + k] - x:
                left = middle + 1
            else:
                right = middle
        return arr[left:left + k]
            