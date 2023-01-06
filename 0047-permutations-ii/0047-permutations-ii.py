class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums_count = {}
        for num in nums:
            nums_count[num] = 1 + nums_count.get(num, 0)
            
        result = []
        def backtracking(combo):
            if len(combo) == len(nums):
                result.append(combo.copy())
                return
            
            for num in nums_count:
                if nums_count[num] == 0:
                    continue
                
                combo.append(num)
                nums_count[num] -= 1
                backtracking(combo)
                
                combo.pop()
                nums_count[num] += 1
            
        backtracking([])
        return result