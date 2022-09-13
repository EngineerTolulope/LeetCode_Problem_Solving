class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        
        def backtracking(current_combo, current_position, target):
            if target == 0:
                result.append(current_combo.copy())
                return
            if target < 0:
                return
            
            previous = -1
            for i in range(current_position, len(candidates)):
                current_candidate = candidates[i]
                if current_candidate == previous:
                    continue
                
                current_combo.append(current_candidate)
                backtracking(current_combo, i + 1, target - current_candidate)
                current_combo.pop()
                
                previous = current_candidate
        backtracking([], 0, target)
        return result
                