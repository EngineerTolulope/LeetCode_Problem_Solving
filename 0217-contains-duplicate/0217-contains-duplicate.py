class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seenNums = set()

        for num in nums:
            if num in seenNums:
                return True
            else:
                seenNums.add(num)
        
        return False