class Solution:
    def interchangeableRectangles(self, rectangles: List[List[int]]) -> int:
        ratio_count = {}
        for width, height in rectangles:
            ratio = width / height
            ratio_count[ratio] = ratio_count.get(ratio, 0) + 1
        
        total_combos = 0
        for count in ratio_count.values():
            if count >= 2:
                total_combos += (count * (count - 1)) // 2 
        return total_combos