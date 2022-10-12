class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        NUMS_LEN = len(nums)
        nums = set(nums)
        
        def backtracking(i, current):
            if i == NUMS_LEN:
                result = "".join(current)
                return result if result not in nums else None
            
            result = backtracking(i + 1, current)
            if result:
                return result
            
            current[i] = '1'
            result = backtracking(i + 1, current)
            if result:
                return result

        return backtracking(0, ['0' for _ in range(NUMS_LEN)])