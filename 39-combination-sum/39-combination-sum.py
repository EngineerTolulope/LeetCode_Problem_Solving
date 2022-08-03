class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        combinations = []
        
        def depth_first_search(i, current_combo, total):
            if total == target:
                combinations.append(current_combo.copy())
                return
            if i >= len(candidates) or total > target:
                return
            
            current_combo.append(candidates[i])
            depth_first_search(i, current_combo, total + candidates[i])
            current_combo.pop()
            depth_first_search(i + 1, current_combo, total)
        
        depth_first_search(0, [], 0)
        return combinations
            
            